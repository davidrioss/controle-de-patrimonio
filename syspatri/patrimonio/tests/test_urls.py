from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from patrimonio.views import (
    listar_bens, adicionar_bem, atualizar_bem, detalhes_bem, excluir_bem,
    listar_categorias, adicionar_categoria, atualizar_categoria, detalhes_categoria, excluir_categoria,
    listar_departamentos, adicionar_departamento, atualizar_departamento, detalhes_departamento, excluir_departamento,
    listar_fornecedores, adicionar_fornecedor, atualizar_fornecedor, detalhes_fornecedor, excluir_fornecedor
)

class URLsTestCase(TestCase):
    def test_listar_bens_url(self):
        self.assertEqual(resolve(reverse('listar_bens')).func, listar_bens)

    def test_adicionar_bem_url(self):
        self.assertEqual(resolve(reverse('adicionar_bem')).func, adicionar_bem)

    def test_atualizar_bem_url(self):
        self.assertEqual(resolve(reverse('atualizar_bem', args=[1])).func, atualizar_bem)

    def test_detalhes_bem_url(self):
        self.assertEqual(resolve(reverse('detalhes_bem', args=[1])).func, detalhes_bem)

    def test_excluir_bem_url(self):
        self.assertEqual(resolve(reverse('excluir_bem', args=[1])).func, excluir_bem)

    def test_listar_categorias_url(self):
        self.assertEqual(resolve(reverse('listar_categorias')).func, listar_categorias)

    def test_adicionar_categoria_url(self):
        self.assertEqual(resolve(reverse('adicionar_categoria')).func, adicionar_categoria)

    def test_atualizar_categoria_url(self):
        self.assertEqual(resolve(reverse('atualizar_categoria', args=[1])).func, atualizar_categoria)

    def test_detalhes_categoria_url(self):
        self.assertEqual(resolve(reverse('detalhes_categoria', args=[1])).func, detalhes_categoria)

    def test_excluir_categoria_url(self):
        self.assertEqual(resolve(reverse('excluir_categoria', args=[1])).func, excluir_categoria)

    def test_listar_departamentos_url(self):
        self.assertEqual(resolve(reverse('listar_departamentos')).func, listar_departamentos)

    def test_adicionar_departamento_url(self):
        self.assertEqual(resolve(reverse('adicionar_departamento')).func, adicionar_departamento)

    def test_atualizar_departamento_url(self):
        self.assertEqual(resolve(reverse('atualizar_departamento', args=[1])).func, atualizar_departamento)

    def test_detalhes_departamento_url(self):
        self.assertEqual(resolve(reverse('detalhes_departamento', args=[1])).func, detalhes_departamento)

    def test_excluir_departamento_url(self):
        self.assertEqual(resolve(reverse('excluir_departamento', args=[1])).func, excluir_departamento)

    def test_listar_fornecedores_url(self):
        self.assertEqual(resolve(reverse('listar_fornecedores')).func, listar_fornecedores)

    def test_adicionar_fornecedor_url(self):
        self.assertEqual(resolve(reverse('adicionar_fornecedor')).func, adicionar_fornecedor)

    def test_atualizar_fornecedor_url(self):
        self.assertEqual(resolve(reverse('atualizar_fornecedor', args=[1])).func, atualizar_fornecedor)

    def test_detalhes_fornecedor_url(self):
        self.assertEqual(resolve(reverse('detalhes_fornecedor', args=[1])).func, detalhes_fornecedor)

    def test_excluir_fornecedor_url(self):
        self.assertEqual(resolve(reverse('excluir_fornecedor', args=[1])).func, excluir_fornecedor)
