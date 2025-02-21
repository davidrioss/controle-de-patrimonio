from django.test import TestCase
from patrimonio.models import Bem, Departamento
from core.models import Usuario
from controle.models import Movimentacao, Manutencao, Auditoria
from datetime import date

class ModelsTestCase(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(username='teste_usuario')
        self.departamento_origem = Departamento.objects.create(nome='TI', responsavel='João', telefone='123456789')
        self.departamento_destino = Departamento.objects.create(nome='RH', responsavel='Maria', telefone='987654321')
        self.bem = Bem.objects.create(nome='Impressora', descricao='Impressora HP', categoria=None,
                                       departamento=self.departamento_origem, fornecedor=None,
                                       data_aquisicao=date.today(), valor=1500.00, rfid='111222333', status='ativo')

    def test_criar_movimentacao(self):
        movimentacao = Movimentacao.objects.create(
            bem=self.bem,
            departamento_origem=self.departamento_origem,
            departamento_destino=self.departamento_destino,
            responsavel=self.usuario,
            observacao='Mudança de setor'
        )
        self.assertEqual(str(movimentacao), f"Movimentação de {self.bem.nome}")

    def test_criar_manutencao(self):
        manutencao = Manutencao.objects.create(
            bem=self.bem,
            data_inicio=date.today(),
            responsavel=self.usuario,
            custo=200.00,
            descricao='Troca de toner'
        )
        self.assertEqual(str(manutencao), f"Manutenção de {self.bem.nome}")

    def test_criar_auditoria(self):
        auditoria = Auditoria.objects.create(
            departamento=self.departamento_origem,
            responsavel=self.usuario,
            observacao='Verificação geral'
        )
        self.assertEqual(str(auditoria), f"Auditoria de {self.departamento_origem.nome} em {auditoria.data}")
