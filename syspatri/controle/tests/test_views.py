from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from controle.models import Movimentacao, Manutencao, Auditoria
from patrimonio.models import Categoria, Departamento, Fornecedor, Bem
from core.models import Usuario
from datetime import date

class ControleViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Criação do usuário com o modelo Usuario
        self.usuario = Usuario.objects.create_user(
            username='testuser',
            password='12345',
            departamento=None,  # Adicione um departamento válido, se necessário
            cargo='Gerente',  # Adicione um cargo válido, se necessário
            gerente=True  # Defina se o usuário é gerente, conforme necessário
        )
        self.client.login(username='testuser', password='12345')
        
        self.categoria = Categoria.objects.create(nome='Eletrônicos', descricao='Equipamentos eletrônicos')
        self.departamento = Departamento.objects.create(nome='TI', responsavel='João', telefone='123456789')
        self.fornecedor = Fornecedor.objects.create(nome='Tech Supplier', cnpj='00.000.000/0001-00')
        self.bem = Bem.objects.create(
            nome='Notebook', descricao='Notebook Dell', categoria=self.categoria,
            departamento=self.departamento, fornecedor=self.fornecedor,
            data_aquisicao=date.today(), valor=5000.00, rfid='123456789', status='ativo'
        )
        
        self.movimentacao = Movimentacao.objects.create(
            bem=self.bem,
            departamento_origem=self.departamento,
            departamento_destino=self.departamento,
            responsavel=self.usuario
        )
        self.manutencao = Manutencao.objects.create(
            bem=self.bem,
            data_inicio='2025-01-01',
            responsavel=self.usuario,
            descricao='Troca de peça'
        )
        self.auditoria = Auditoria.objects.create(
            departamento=self.departamento,
            responsavel=self.usuario,
            observacao='Verificação de equipamentos'
        )

    def test_listar_movimentacoes(self):
        response = self.client.get(reverse('listar_movimentacoes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listar_movimentacoes.html')

    def test_adicionar_movimentacao(self):
        response = self.client.post(reverse('adicionar_movimentacao'), {
            'bem': self.bem.id,
            'departamento_origem': self.departamento.id,
            'departamento_destino': self.departamento.id,
            'responsavel': self.usuario.id,
            'observacao': 'Movimentação de teste'
        })
        self.assertEqual(response.status_code, 302)

    def test_atualizar_movimentacao(self):
        response = self.client.post(reverse('atualizar_movimentacao', args=[self.movimentacao.id]), {
            'bem': self.bem.id,
            'departamento_origem': self.departamento.id,
            'departamento_destino': self.departamento.id,
            'responsavel': self.usuario.id,
            'observacao': 'Atualizado'
        })
        self.assertEqual(response.status_code, 302)

    def test_excluir_movimentacao(self):
        response = self.client.post(reverse('excluir_movimentacao', args=[self.movimentacao.id]))
        self.assertEqual(response.status_code, 302)

    def test_listar_manutencoes(self):
        response = self.client.get(reverse('listar_manutencoes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listar_manutencoes.html')

    def test_adicionar_manutencao(self):
        response = self.client.post(reverse('adicionar_manutencao'), {
            'bem': self.bem.id,
            'data_inicio': '2025-01-02',
            'responsavel': self.usuario.id,
            'descricao': 'Nova manutenção'
        })
        self.assertEqual(response.status_code, 302)

    def test_excluir_manutencao(self):
        response = self.client.post(reverse('excluir_manutencao', args=[self.manutencao.id]))
        self.assertEqual(response.status_code, 302)

    def test_listar_auditorias(self):
        response = self.client.get(reverse('listar_auditorias'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listar_auditorias.html')

    def test_adicionar_auditoria(self):
        response = self.client.post(reverse('adicionar_auditoria'), {
            'departamento': self.departamento.id,
            'responsavel': self.usuario.id,
            'observacao': 'Nova auditoria'
        })
        self.assertEqual(response.status_code, 302)

    def test_excluir_auditoria(self):
        response = self.client.post(reverse('excluir_auditoria', args=[self.auditoria.id]))
        self.assertEqual(response.status_code, 302)
