from django.test import TestCase
from controle.forms import MovimentacaoForm, ManutencaoForm, AuditoriaForm
from patrimonio.models import Bem, Departamento
from core.models import Usuario
from controle.models import Movimentacao, Manutencao, Auditoria
from datetime import date

class FormsTestCase(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(username='testuser')
        self.departamento_origem = Departamento.objects.create(nome='TI', responsavel='João', telefone='123456789')
        self.departamento_destino = Departamento.objects.create(nome='RH', responsavel='Maria', telefone='987654321')
        self.bem = Bem.objects.create(
            nome='Notebook', descricao='Notebook Dell', categoria=None,
            departamento=self.departamento_origem, fornecedor=None,
            data_aquisicao=date.today(), valor=5000.00, rfid='123456789', status='ativo'
        )
    
    def test_movimentacao_form_valid(self):
        form_data = {
            'bem': self.bem.id,
            'departamento_origem': self.departamento_origem.id,
            'departamento_destino': self.departamento_destino.id,
            'responsavel': self.usuario.id,
            'observacao': 'Transferência interna'
        }
        form = MovimentacaoForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_manutencao_form_valid(self):
        form_data = {
            'bem': self.bem.id,
            'data_inicio': '2025-02-01',
            'data_fim': '2025-02-10',
            'responsavel': self.usuario.id,
            'custo': '500.00',
            'descricao': 'Troca de bateria'
        }
        form = ManutencaoForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_auditoria_form_valid(self):
        form_data = {
            'departamento': self.departamento_origem.id,
            'responsavel': self.usuario.id,
            'observacao': 'Verificação de bens'
        }
        form = AuditoriaForm(data=form_data)
        self.assertTrue(form.is_valid())
