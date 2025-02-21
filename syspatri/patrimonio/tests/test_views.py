from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from patrimonio.models import Bem, Categoria, Departamento, Fornecedor
from datetime import date
from core.models import Usuario

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = Usuario.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

        self.categoria = Categoria.objects.create(nome='Eletrônicos', descricao='Equipamentos eletrônicos')
        self.departamento = Departamento.objects.create(nome='TI', responsavel='João', telefone='123456789')
        self.fornecedor = Fornecedor.objects.create(nome='Tech Supplier', cnpj='00.000.000/0001-00')
        self.bem = Bem.objects.create(
            nome='Notebook', descricao='Notebook Dell', categoria=self.categoria,
            departamento=self.departamento, fornecedor=self.fornecedor,
            data_aquisicao=date.today(), valor=5000.00, rfid='123456789', status='ativo'
        )
    
    # Testes para Bens
    def test_listar_bens(self):
        response = self.client.get(reverse('listar_bens'))
        self.assertEqual(response.status_code, 200)

    def test_adicionar_bem(self):
        response = self.client.post(reverse('adicionar_bem'), {
            'nome': 'Monitor', 'descricao': 'Monitor 27"', 'categoria': self.categoria.id,
            'departamento': self.departamento.id, 'fornecedor': self.fornecedor.id,
            'data_aquisicao': '2025-01-01', 'valor': '1200.00', 'rfid': '987654321', 'status': 'ativo'
        })
        self.assertEqual(response.status_code, 302)

    def test_atualizar_bem(self):
        response = self.client.post(reverse('atualizar_bem', args=[self.bem.id]), {
            'nome': 'Notebook Gamer', 'descricao': 'Notebook atualizado', 'categoria': self.categoria.id,
            'departamento': self.departamento.id, 'fornecedor': self.fornecedor.id,
            'data_aquisicao': '2025-01-01', 'valor': '6000.00', 'rfid': '123456789', 'status': 'ativo'
        })
        self.assertEqual(response.status_code, 302)

    def test_excluir_bem(self):
        response = self.client.post(reverse('excluir_bem', args=[self.bem.id]))
        self.assertEqual(response.status_code, 302)
    
    def test_detalhes_bem(self):
        response = self.client.get(reverse('detalhes_bem', args=[self.bem.id]))
        self.assertEqual(response.status_code, 200)
    
    # Testes para Categorias
    def test_listar_categorias(self):
        response = self.client.get(reverse('listar_categorias'))
        self.assertEqual(response.status_code, 200)
    
    def test_adicionar_categoria(self):
        response = self.client.post(reverse('adicionar_categoria'), {'nome': 'Móveis', 'descricao': 'Móveis de escritório'})
        self.assertEqual(response.status_code, 302)
    
    def test_atualizar_categoria(self):
        response = self.client.post(reverse('atualizar_categoria', args=[self.categoria.id]), {'nome': 'Eletrônicos Atualizados'})
        self.assertEqual(response.status_code, 302)
    
    def test_excluir_categoria(self):
        response = self.client.post(reverse('excluir_categoria', args=[self.categoria.id]))
        self.assertEqual(response.status_code, 302)
    
    # Testes para Departamentos
    def test_listar_departamentos(self):
        response = self.client.get(reverse('listar_departamentos'))
        self.assertEqual(response.status_code, 200)
    
    def test_adicionar_departamento(self):
        response = self.client.post(reverse('adicionar_departamento'), {
            'nome': 'RH', 'responsavel': 'Maria', 'telefone': '987654321'
        })
        self.assertEqual(response.status_code, 302)
    """
    def test_atualizar_departamento(self):
        response = self.client.post(reverse('atualizar_departamento', args=[self.departamento.id]), {'nome': 'TI Atualizado'})
        self.assertEqual(response.status_code, 302)
    """
    def test_excluir_departamento(self):
        response = self.client.post(reverse('excluir_departamento', args=[self.departamento.id]))
        self.assertEqual(response.status_code, 302)
    
    # Testes para Fornecedores
    def test_listar_fornecedores(self):
        response = self.client.get(reverse('listar_fornecedores'))
        self.assertEqual(response.status_code, 200)
    
    def test_adicionar_fornecedor(self):
        response = self.client.post(reverse('adicionar_fornecedor'), {
            'nome': 'Nova Empresa', 'cnpj': '11.111.111/0001-11', 'telefone': '40028922', 'email': 'contato@empresa.com'
        })
        self.assertEqual(response.status_code, 302)
    """
    def test_atualizar_fornecedor(self):
        response = self.client.post(reverse('atualizar_fornecedor', args=[self.fornecedor.id]), {
            'nome': 'Fornecedor Atualizado'
        })
        self.assertEqual(response.status_code, 302)
    """
    def test_excluir_fornecedor(self):
        response = self.client.post(reverse('excluir_fornecedor', args=[self.fornecedor.id]))
        self.assertEqual(response.status_code, 302)
