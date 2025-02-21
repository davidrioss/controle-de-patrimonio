from django.test import SimpleTestCase
from django.urls import reverse, resolve
from controle import views

class TestUrls(SimpleTestCase):
    
    def test_listar_movimentacoes_url_resolves(self):
        url = reverse('listar_movimentacoes')
        self.assertEqual(resolve(url).func, views.listar_movimentacoes)
    
    def test_adicionar_movimentacao_url_resolves(self):
        url = reverse('adicionar_movimentacao')
        self.assertEqual(resolve(url).func, views.adicionar_movimentacao)
    
    def test_atualizar_movimentacao_url_resolves(self):
        url = reverse('atualizar_movimentacao', args=[1])
        self.assertEqual(resolve(url).func, views.atualizar_movimentacao)
    
    def test_detalhes_movimentacao_url_resolves(self):
        url = reverse('detalhes_movimentacao', args=[1])
        self.assertEqual(resolve(url).func, views.detalhes_movimentacao)
    
    def test_excluir_movimentacao_url_resolves(self):
        url = reverse('excluir_movimentacao', args=[1])
        self.assertEqual(resolve(url).func, views.excluir_movimentacao)
    
    def test_listar_manutencoes_url_resolves(self):
        url = reverse('listar_manutencoes')
        self.assertEqual(resolve(url).func, views.listar_manutencoes)
    
    def test_adicionar_manutencao_url_resolves(self):
        url = reverse('adicionar_manutencao')
        self.assertEqual(resolve(url).func, views.adicionar_manutencao)
    
    def test_atualizar_manutencao_url_resolves(self):
        url = reverse('atualizar_manutencao', args=[1])
        self.assertEqual(resolve(url).func, views.atualizar_manutencao)
    
    def test_detalhes_manutencao_url_resolves(self):
        url = reverse('detalhes_manutencao', args=[1])
        self.assertEqual(resolve(url).func, views.detalhes_manutencao)
    
    def test_excluir_manutencao_url_resolves(self):
        url = reverse('excluir_manutencao', args=[1])
        self.assertEqual(resolve(url).func, views.excluir_manutencao)
    
    def test_listar_auditorias_url_resolves(self):
        url = reverse('listar_auditorias')
        self.assertEqual(resolve(url).func, views.listar_auditorias)
    
    def test_adicionar_auditoria_url_resolves(self):
        url = reverse('adicionar_auditoria')
        self.assertEqual(resolve(url).func, views.adicionar_auditoria)
    
    def test_atualizar_auditoria_url_resolves(self):
        url = reverse('atualizar_auditoria', args=[1])
        self.assertEqual(resolve(url).func, views.atualizar_auditoria)
    
    def test_detalhes_auditoria_url_resolves(self):
        url = reverse('detalhes_auditoria', args=[1])
        self.assertEqual(resolve(url).func, views.detalhes_auditoria)
    
    def test_excluir_auditoria_url_resolves(self):
        url = reverse('excluir_auditoria', args=[1])
        self.assertEqual(resolve(url).func, views.excluir_auditoria)