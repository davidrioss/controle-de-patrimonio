from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Movimentacao, Manutencao, Auditoria
from .forms import MovimentacaoForm, ManutencaoForm, AuditoriaForm
from patrimonio.models import Bem, Departamento
from core.models import Usuario

# -----------------------------views relacionadas às movimentações-----------------------------

@login_required
def listar_movimentacoes(request):
    """
    View para listar todas as movimentações cadastradas.
    """
    movimentacoes = Movimentacao.objects.all().order_by('-data_movimentacao')
    paginator = Paginator(movimentacoes, 20)  # Exibe 20 movimentações por página
    page_number = request.GET.get('page')  # Obtém o número da página atual
    page_obj = paginator.get_page(page_number)  # Obtém as movimentações para a página atual
    return render(request, 'listar_movimentacoes.html', {'page_obj': page_obj})

@login_required
def adicionar_movimentacao(request):
    """
    View para adicionar uma nova movimentação.
    """
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Movimentação cadastrada com sucesso!')
            return redirect('listar_movimentacoes')
    else:
        form = MovimentacaoForm()
    return render(request, 'adicionar_movimentacao.html', {'form': form})

@login_required
def atualizar_movimentacao(request, pk):
    """
    View para editar uma movimentação existente.
    """
    movimentacao = get_object_or_404(Movimentacao, pk=pk)
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST, instance=movimentacao)
        if form.is_valid():
            form.save()
            messages.success(request, 'Movimentação atualizada com sucesso!')
            return redirect('listar_movimentacoes')
    else:
        form = MovimentacaoForm(instance=movimentacao)
    return render(request, 'atualizar_movimentacao.html', {'form': form, 'movimentacao': movimentacao})

@login_required
def detalhes_movimentacao(request, pk):
    """
    View para exibir detalhes de uma movimentação.
    """
    movimentacao = get_object_or_404(Movimentacao, pk=pk)
    return render(request, 'detalhes_movimentacao.html', {'movimentacao': movimentacao})

@login_required
def excluir_movimentacao(request, pk):
    """
    View para excluir uma movimentação.
    """
    movimentacao = get_object_or_404(Movimentacao, pk=pk)
    if request.method in ['POST', 'GET']:
        movimentacao.delete()
        messages.success(request, 'Movimentação excluída com sucesso!')
        return redirect('listar_movimentacoes')

# -----------------------------views relacionadas às manutenções-----------------------------

@login_required
def listar_manutencoes(request):
    """
    View para listar todas as manutenções cadastradas.
    """
    manutencoes = Manutencao.objects.all().order_by('-data_inicio')
    paginator = Paginator(manutencoes, 20)  # Exibe 20 manutenções por página
    page_number = request.GET.get('page')  # Obtém o número da página atual
    page_obj = paginator.get_page(page_number)  # Obtém as manutenções para a página atual
    return render(request, 'listar_manutencoes.html', {'page_obj': page_obj})

@login_required
def adicionar_manutencao(request):
    """
    View para adicionar uma nova manutenção.
    """
    if request.method == 'POST':
        form = ManutencaoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Manutenção cadastrada com sucesso!')
            return redirect('listar_manutencoes')
    else:
        form = ManutencaoForm()
    return render(request, 'adicionar_manutencao.html', {'form': form})

@login_required
def atualizar_manutencao(request, pk):
    """
    View para editar uma manutenção existente.
    """
    manutencao = get_object_or_404(Manutencao, pk=pk)
    if request.method == 'POST':
        form = ManutencaoForm(request.POST, instance=manutencao)
        if form.is_valid():
            form.save()
            messages.success(request, 'Manutenção atualizada com sucesso!')
            return redirect('listar_manutencoes')
    else:
        form = ManutencaoForm(instance=manutencao)
    return render(request, 'atualizar_manutencao.html', {'form': form, 'manutencao': manutencao})

@login_required
def detalhes_manutencao(request, pk):
    """
    View para exibir detalhes de uma manutenção.
    """
    manutencao = get_object_or_404(Manutencao, pk=pk)
    return render(request, 'detalhes_manutencao.html', {'manutencao': manutencao})

@login_required
def excluir_manutencao(request, pk):
    """
    View para excluir uma manutenção.
    """
    manutencao = get_object_or_404(Manutencao, pk=pk)
    if request.method in ['POST', 'GET']:
        manutencao.delete()
        messages.success(request, 'Manutenção excluída com sucesso!')
        return redirect('listar_manutencoes')

# -----------------------------views relacionadas às auditorias-----------------------------

@login_required
def listar_auditorias(request):
    """
    View para listar todas as auditorias cadastradas.
    """
    auditorias = Auditoria.objects.all().order_by('-data')
    paginator = Paginator(auditorias, 20)  # Exibe 20 auditorias por página
    page_number = request.GET.get('page')  # Obtém o número da página atual
    page_obj = paginator.get_page(page_number)  # Obtém as auditorias para a página atual
    return render(request, 'listar_auditorias.html', {'page_obj': page_obj})

@login_required
def adicionar_auditoria(request):
    """
    View para adicionar uma nova auditoria.
    """
    if request.method == 'POST':
        form = AuditoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Auditoria cadastrada com sucesso!')
            return redirect('listar_auditorias')
    else:
        form = AuditoriaForm()
    return render(request, 'adicionar_auditoria.html', {'form': form})

@login_required
def atualizar_auditoria(request, pk):
    """
    View para editar uma auditoria existente.
    """
    auditoria = get_object_or_404(Auditoria, pk=pk)
    if request.method == 'POST':
        form = AuditoriaForm(request.POST, instance=auditoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Auditoria atualizada com sucesso!')
            return redirect('listar_auditorias')
    else:
        form = AuditoriaForm(instance=auditoria)
    return render(request, 'atualizar_auditoria.html', {'form': form, 'auditoria': auditoria})

@login_required
def detalhes_auditoria(request, pk):
    """
    View para exibir detalhes de uma auditoria.
    """
    auditoria = get_object_or_404(Auditoria, pk=pk)
    return render(request, 'detalhes_auditoria.html', {'auditoria': auditoria})

@login_required
def excluir_auditoria(request, pk):
    """
    View para excluir uma auditoria.
    """
    auditoria = get_object_or_404(Auditoria, pk=pk)
    if request.method in ['POST', 'GET']:
        auditoria.delete()
        messages.success(request, 'Auditoria excluída com sucesso!')
        return redirect('listar_auditorias')