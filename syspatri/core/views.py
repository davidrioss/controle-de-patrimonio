from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Usuario
from .forms import UsuarioCreationForm, UsuarioChangeForm, LoginForm
from patrimonio.models import Bem, Categoria, Departamento, Fornecedor
from controle.models import Movimentacao, Manutencao, Auditoria

# -----------------------------views relacionadas ao dashboard-----------------------------

@login_required
def dashboard(request):
    """
    View para exibir o dashboard da aplicação.
    """
    total_bens = Bem.objects.count()
    total_categorias = Categoria.objects.count()
    total_departamentos = Departamento.objects.count()
    total_fornecedores = Fornecedor.objects.count()
    total_movimentacoes = Movimentacao.objects.count()
    total_manutencoes = Manutencao.objects.count()
    total_auditorias = Auditoria.objects.count()

    context = {
        'total_bens': total_bens,
        'total_categorias': total_categorias,
        'total_departamentos': total_departamentos,
        'total_fornecedores': total_fornecedores,
        'total_movimentacoes': total_movimentacoes,
        'total_manutencoes': total_manutencoes,
        'total_auditorias': total_auditorias,
    }
    return render(request, 'dashboard.html', context)

# -----------------------------views relacionadas aos usuários-----------------------------

@login_required
def listar_usuarios(request):
    """
    View para listar todos os usuários do sistema.
    """
    usuarios = Usuario.objects.all().order_by('username')
    paginator = Paginator(usuarios, 20)  # Exibe 20 usuários por página
    page_number = request.GET.get('page')  # Obtém o número da página atual
    page_obj = paginator.get_page(page_number)  # Obtém os usuários para a página atual
    return render(request, 'listar_usuarios.html', {'page_obj': page_obj})

@login_required
def adicionar_usuario(request):
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
def atualizar_usuario(request, pk):
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
def detalhes_usuario(request, pk):
    """
    View para exibir detalhes de um usuário.
    """
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'detalhes_usuario.html', {'usuario': usuario})

@login_required
def excluir_usuario(request, pk):
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

# -----------------------------views relacionadas ao registro de usuários-----------------------------

def registro(request):
    """
    View para registro de novos usuários.
    """
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado com sucesso! Faça login para continuar.')
            return redirect('login')
    else:
        form = UsuarioCreationForm()
    return render(request, 'registro.html', {'form': form})

