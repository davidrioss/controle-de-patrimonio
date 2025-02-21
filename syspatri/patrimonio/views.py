from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Bem, Categoria, Departamento, Fornecedor
from .forms import BemForm, CategoriaForm, DepartamentoForm, FornecedorForm

# -----------------------------views relacionadas aos bens-----------------------------

@login_required
def listar_bens(request):
    """
    View para listar todos os bens cadastrados.
    """
    bens = Bem.objects.all().order_by('nome')
    paginator = Paginator(bens, 20)  # Exibe 20 bens por página
    page_number = request.GET.get('page')  # Obtém o número da página atual
    page_obj = paginator.get_page(page_number)  # Obtém os bens para a página atual
    return render(request, 'listar_bens.html', {'page_obj': page_obj})

@login_required
def adicionar_bem(request):
    """
    View para adicionar um novo bem.
    """
    if request.method == 'POST':
        form = BemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bem cadastrado com sucesso!')
            return redirect('listar_bens')
    else:
        form = BemForm()
    return render(request, 'adicionar_bem.html', {'form': form})

@login_required
def atualizar_bem(request, pk):
    """
    View para editar um bem existente.
    """
    bem = get_object_or_404(Bem, pk=pk)
    if request.method == 'POST':
        form = BemForm(request.POST, instance=bem)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bem atualizado com sucesso!')
            return redirect('listar_bens')
    else:
        form = BemForm(instance=bem)
    return render(request, 'atualizar_bem.html', {'form': form, 'bem': bem})

@login_required
def detalhes_bem(request, pk):
    """
    View para exibir detalhes de um bem.
    """
    bem = get_object_or_404(Bem, pk=pk)
    return render(request, 'detalhes_bem.html', {'bem': bem})

@login_required
def excluir_bem(request, pk):
    """
    View para excluir um bem.
    """
    bem = get_object_or_404(Bem, pk=pk)
    if request.method in ['POST', 'GET']:
        bem.delete()
        messages.success(request, 'Bem excluído com sucesso!')
        return redirect('listar_bens')

# -----------------------------views relacionadas às categorias-----------------------------

@login_required
def listar_categorias(request):
    """
    View para listar todas as categorias cadastradas.
    """
    categorias = Categoria.objects.all().order_by('nome')
    paginator = Paginator(categorias, 20)  # Exibe 20 categorias por página
    page_number = request.GET.get('page')  # Obtém o número da página atual
    page_obj = paginator.get_page(page_number)  # Obtém as categorias para a página atual
    return render(request, 'listar_categorias.html', {'page_obj': page_obj})

@login_required
def adicionar_categoria(request):
    """
    View para adicionar uma nova categoria.
    """
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria cadastrada com sucesso!')
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'adicionar_categoria.html', {'form': form})

@login_required
def atualizar_categoria(request, pk):
    """
    View para editar uma categoria existente.
    """
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria atualizada com sucesso!')
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'atualizar_categoria.html', {'form': form, 'categoria': categoria})

@login_required
def detalhes_categoria(request, pk):
    """
    View para exibir detalhes de uma categoria.
    """
    categoria = get_object_or_404(Categoria, pk=pk)
    bens = Bem.objects.filter(categoria=categoria)  # Filtra os bens por categoria
    context = {
        'categoria': categoria,
        'bens': bens,  # Passa os bens para o template
    }
    return render(request, 'detalhes_categoria.html', context)

@login_required
def excluir_categoria(request, pk):
    """
    View para excluir uma categoria.
    """
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method in ['POST', 'GET']:
        categoria.delete()
        messages.success(request, 'Categoria excluída com sucesso!')
        return redirect('listar_categorias')

# -----------------------------views relacionadas aos departamentos-----------------------------

@login_required
def listar_departamentos(request):
    """
    View para listar todos os departamentos cadastrados.
    """
    departamentos = Departamento.objects.all().order_by('nome')
    paginator = Paginator(departamentos, 20)  # Exibe 20 departamentos por página
    page_number = request.GET.get('page')  # Obtém o número da página atual
    page_obj = paginator.get_page(page_number)  # Obtém os departamentos para a página atual
    return render(request, 'listar_departamentos.html', {'page_obj': page_obj})

@login_required
def adicionar_departamento(request):
    """
    View para adicionar um novo departamento.
    """
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Departamento cadastrado com sucesso!')
            return redirect('listar_departamentos')
    else:
        form = DepartamentoForm()
    return render(request, 'adicionar_departamento.html', {'form': form})

@login_required
def atualizar_departamento(request, pk):
    """
    View para editar um departamento existente.
    """
    departamento = get_object_or_404(Departamento, pk=pk)
    if request.method == 'POST':
        form = DepartamentoForm(request.POST, instance=departamento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Departamento atualizado com sucesso!')
            return redirect('listar_departamentos')
    else:
        form = DepartamentoForm(instance=departamento)
    return render(request, 'atualizar_departamento.html', {'form': form, 'departamento': departamento})

@login_required
def detalhes_departamento(request, pk):
    """
    View para exibir detalhes de um departamento.
    """
    departamento = get_object_or_404(Departamento, pk=pk)
    bens = Bem.objects.filter(departamento=departamento)  # Filtra os bens do departamento
    context = {
        'departamento': departamento,
        'bens': bens,  # Passa os bens para o template
    }
    return render(request, 'detalhes_departamento.html', context)

@login_required
def excluir_departamento(request, pk):
    """
    View para excluir um departamento.
    """
    departamento = get_object_or_404(Departamento, pk=pk)
    if request.method in ['POST', 'GET']:
        departamento.delete()
        messages.success(request, 'Departamento excluído com sucesso!')
        return redirect('listar_departamentos')

# -----------------------------views relacionadas aos fornecedores-----------------------------

@login_required
def listar_fornecedores(request):
    """
    View para listar todos os fornecedores cadastrados.
    """
    fornecedores = Fornecedor.objects.all().order_by('nome')
    paginator = Paginator(fornecedores, 20)  # Exibe 20 fornecedores por página
    page_number = request.GET.get('page')  # Obtém o número da página atual
    page_obj = paginator.get_page(page_number)  # Obtém os fornecedores para a página atual
    return render(request, 'listar_fornecedores.html', {'page_obj': page_obj})

@login_required
def adicionar_fornecedor(request):
    """
    View para adicionar um novo fornecedor.
    """
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fornecedor cadastrado com sucesso!')
            return redirect('listar_fornecedores')
    else:
        form = FornecedorForm()
    return render(request, 'adicionar_fornecedor.html', {'form': form})

@login_required
def atualizar_fornecedor(request, pk):
    """
    View para editar um fornecedor existente.
    """
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    if request.method == 'POST':
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fornecedor atualizado com sucesso!')
            return redirect('listar_fornecedores')
    else:
        form = FornecedorForm(instance=fornecedor)
    return render(request, 'atualizar_fornecedor.html', {'form': form, 'fornecedor': fornecedor})

@login_required
def detalhes_fornecedor(request, pk):
    """
    View para exibir detalhes de um fornecedor.
    """
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    return render(request, 'detalhes_fornecedor.html', {'fornecedor': fornecedor})

@login_required
def excluir_fornecedor(request, pk):
    """
    View para excluir um fornecedor.
    """
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    if request.method in ['POST', 'GET']:
        fornecedor.delete()
        messages.success(request, 'Fornecedor excluído com sucesso!')
        return redirect('listar_fornecedores')
    
    
    
    
