from django.test import TestCase
from patrimonio.forms import BemForm, CategoriaForm, DepartamentoForm, FornecedorForm
from patrimonio.models import Categoria, Departamento, Fornecedor

class BemFormTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome="Eletrônicos")
        self.departamento = Departamento.objects.create(nome="TI", responsavel="João Silva")
        self.fornecedor = Fornecedor.objects.create(nome="Fornecedor XYZ", cnpj="12.345.678/0001-99")

    def test_bem_form_valido(self):
        """Testa se o formulário de Bem é válido com dados corretos."""
        form_data = {
            'nome': 'Notebook',
            'descricao': 'Notebook Dell',
            'categoria': self.categoria.id,
            'departamento': self.departamento.id,
            'fornecedor': self.fornecedor.id,
            'data_aquisicao': '2023-01-01',
            'valor': 5000,
            'rfid': '1234567890',
            'status': 'ativo'
        }
        form = BemForm(data=form_data)
        self.assertTrue(form.is_valid())

    """
    def test_bem_form_invalido(self):
        #Testa se o formulário de Bem é inválido com dados incorretos.
        form_data = {
            'nome': '',  # Campo obrigatório
            'descricao': 'Notebook Dell',
            'categoria': self.categoria.id,
            'departamento': self.departamento.id,
            'fornecedor': self.fornecedor.id,
            'data_aquisicao': '2023-01-01',
            'valor': -100.00,  # Valor negativo
            'rfid': '1234567890',
            'status': 'ativo'
        }
        form = BemForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('nome', form.errors)
        self.assertIn('valor', form.errors)
    """

class CategoriaFormTest(TestCase):
    def test_categoria_form_valido(self):
        """Testa se o formulário de Categoria é válido com dados corretos."""
        form_data = {
            'nome': 'Eletrônicos',
            'descricao': 'Categoria de eletrônicos'
        }
        form = CategoriaForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_categoria_form_invalido(self):
        """Testa se o formulário de Categoria é inválido com dados incorretos."""
        form_data = {
            'nome': '',  # Campo obrigatório
            'descricao': 'Categoria de eletrônicos'
        }
        form = CategoriaForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('nome', form.errors)

class DepartamentoFormTest(TestCase):
    def test_departamento_form_valido(self):
        """Testa se o formulário de Departamento é válido com dados corretos."""
        form_data = {
            'nome': 'TI',
            'responsavel': 'João Silva',
            'telefone': '(11) 99999-9999'
        }
        form = DepartamentoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_departamento_form_invalido(self):
        """Testa se o formulário de Departamento é inválido com dados incorretos."""
        form_data = {
            'nome': '',  # Campo obrigatório
            'responsavel': 'João Silva',
            'telefone': '(11) 99999-9999'
        }
        form = DepartamentoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('nome', form.errors)

class FornecedorFormTest(TestCase):
    def test_fornecedor_form_valido(self):
        """Testa se o formulário de Fornecedor é válido com dados corretos."""
        form_data = {
            'nome': 'Fornecedor XYZ',
            'cnpj': '12.345.678/0001-99',
            'telefone': '(11) 99999-9999',
            'email': 'contato@fornecedorxyz.com'
        }
        form = FornecedorForm(data=form_data)
        self.assertTrue(form.is_valid())

"""
    def test_fornecedor_form_invalido(self):
        #Testa se o formulário de Fornecedor é inválido com dados incorretos.
        form_data = {
            'nome': 'Fornecedor XYZ',
            'cnpj': '123',  # CNPJ inválido
            'telefone': '(11) 99999-9999',
            'email': 'contato@fornecedorxyz.com'
        }
        form = FornecedorForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('cnpj', form.errors)
"""