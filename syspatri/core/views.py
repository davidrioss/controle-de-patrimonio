from itertools import count
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator
from django.db.models import Count, Sum, Q
from .models import Usuario
from .forms import UsuarioCreationForm, UsuarioChangeForm, LoginForm
from patrimonio.models import Bem, Categoria, Departamento, Fornecedor
from controle.models import Movimentacao, Manutencao, Auditoria
from datetime import datetime, timedelta
import json

# -----------------------------views relacionadas ao dashboard-----------------------------

@login_required
def dashboard(request):
    # Métricas principais
    total_bens = Bem.objects.count()
    total_departamentos = Departamento.objects.count()
    total_manutencoes_ativas = Manutencao.objects.filter(data_fim__isnull=True).count()
    valor_total_patrimonio = Bem.objects.aggregate(total=Sum('valor'))['total'] or 0

    # Dados para o gráfico de bens por departamento
    departamentos = Departamento.objects.annotate(total_bens=Count('bem')).values_list('nome', flat=True)
    bens_por_departamento = Departamento.objects.annotate(total_bens=Count('bem')).values_list('total_bens', flat=True)

    # Dados para o gráfico de bens por categoria
    categorias = Categoria.objects.annotate(total_bens=Count('bem')).values_list('nome', flat=True)
    bens_por_categoria = Categoria.objects.annotate(total_bens=Count('bem')).values_list('total_bens', flat=True)

    # Dados para o gráfico de histórico de manutenções
    meses = []
    manutencoes_por_mes = []
    for i in range(12):
        mes = datetime.now() - timedelta(days=30 * i)
        total = Manutencao.objects.filter(data_inicio__month=mes.month, data_inicio__year=mes.year).count()
        meses.append(mes.strftime('%b'))  # Nome abreviado do mês (ex: Jan, Fev)
        manutencoes_por_mes.append(total)
    meses.reverse()
    manutencoes_por_mes.reverse()
        
    # Dados para o gráfico de histórico de manutenções
    meses = []
    manutencoes_custo_por_mes = []
    for i in range(12):
        mes = datetime.now() - timedelta(days=30 * i)
        total_custo = Manutencao.objects.filter(
            data_inicio__month=mes.month, 
            data_inicio__year=mes.year
        ).aggregate(Sum('custo'))['custo__sum'] or 0  # Soma dos custos, se não houver, retorna 0
        
        meses.append(mes.strftime('%b'))  # Nome abreviado do mês (ex: Jan, Fev)
        manutencoes_custo_por_mes.append(float(total_custo))  # Converte para float

    meses.reverse()
    manutencoes_custo_por_mes.reverse()

    # Manutenções recentes
    manutencoes_recentes = Manutencao.objects.order_by('-data_inicio')[:10]

    context = {
        'total_bens': total_bens,
        'total_departamentos': total_departamentos,
        'total_manutencoes_ativas': total_manutencoes_ativas,
        'valor_total_patrimonio': valor_total_patrimonio,
        'departamentos': list(departamentos),
        'bens_por_departamento': list(bens_por_departamento),
        'categorias': list(categorias),
        'bens_por_categoria': list(bens_por_categoria),
        'meses': meses,
        'manutencoes_por_mes': manutencoes_por_mes,
        'manutencoes_custo_por_mes': manutencoes_custo_por_mes,  # Agora só contém floats
        'manutencoes_recentes': manutencoes_recentes,
    }

    return render(request, 'dashboard.html', context)


# -----------------------------views relacionadas aos usuários-----------------------------

def is_superuser_or_gerente(user):
    return user.is_superuser or user.gerente

@login_required
@user_passes_test(is_superuser_or_gerente, login_url='login')
def listar_usuarios(request):
    if not request.user.is_superuser and not request.user.gerente:
        raise PermissionDenied
    """
    View para listar todos os usuários do sistema.
    """
    usuarios = Usuario.objects.all().order_by('username')
    paginator = Paginator(usuarios, 20)  # Exibe 20 usuários por página
    page_number = request.GET.get('page')  # Obtém o número da página atual
    page_obj = paginator.get_page(page_number)  # Obtém os usuários para a página atual
    return render(request, 'listar_usuarios.html', {'page_obj': page_obj})

@login_required
@user_passes_test(is_superuser_or_gerente, login_url='login')
def adicionar_usuario(request):
    if not request.user.is_superuser and not request.user.gerente:
        raise PermissionDenied
    """
    View para adicionar um novo usuário.
    """
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('listar_usuarios')
    else:
        form = UsuarioCreationForm()
    return render(request, 'adicionar_usuario.html', {'form': form})

@login_required
@user_passes_test(is_superuser_or_gerente, login_url='login')
def atualizar_usuario(request, pk):
    if not request.user.is_superuser and not request.user.gerente:
        raise PermissionDenied
    """
    View para editar um usuário existente.
    """
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioChangeForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário atualizado com sucesso!')
            return redirect('listar_usuarios')
    else:
        form = UsuarioChangeForm(instance=usuario)
    return render(request, 'atualizar_usuario.html', {'form': form, 'usuario': usuario})

@login_required
@user_passes_test(is_superuser_or_gerente, login_url='login')
def detalhes_usuario(request, pk):
    if not request.user.is_superuser and not request.user.gerente:
        raise PermissionDenied
    """
    View para exibir detalhes de um usuário.
    """
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'detalhes_usuario.html', {'usuario': usuario})

@login_required
@user_passes_test(is_superuser_or_gerente, login_url='login')
def excluir_usuario(request, pk):
    if not request.user.is_superuser and not request.user.gerente:
        raise PermissionDenied
    """
    View para excluir um usuário.
    """
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method in ['POST', 'GET']:
        usuario.delete()
        messages.success(request, 'Usuário excluído com sucesso!')
        return redirect('listar_usuarios')

# -----------------------------views relacionadas à autenticação-----------------------------

def custom_login(request):
    """
    View para autenticação de usuários.
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Usuário ou senha incorretos.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def custom_logout(request):
    """
    View para logout de usuários.
    """
    logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('login')

@login_required
def perfil_usuario(request):
    """
    View para exibir e editar o perfil do usuário logado.
    """
    usuario = request.user
    if request.method == 'POST':
        form = UsuarioChangeForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('perfil_usuario')
    else:
        form = UsuarioChangeForm(instance=usuario)
    return render(request, 'perfil.html', {'form': form})

