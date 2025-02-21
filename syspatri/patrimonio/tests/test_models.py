from django.test import TestCase
from patrimonio.models import Categoria, Departamento, Fornecedor, Bem
from django.core.exceptions import ValidationError
from datetime import date

class CategoriaModelTest(TestCase):
    def test_criar_categoria(self):
        """Testa a criação de uma categoria."""
        categoria = Categoria.objects.create(nome="Eletrônicos", descricao="Categoria de eletrônicos")
        self.assertEqual(categoria.nome, "Eletrônicos")
        self.assertEqual(categoria.descricao, "Categoria de eletrônicos")
        self.assertEqual(str(categoria), "Eletrônicos")

class DepartamentoModelTest(TestCase):
    def test_criar_departamento(self):
        """Testa a criação de um departamento."""
        departamento = Departamento.objects.create(
            nome="TI",
            responsavel="João Silva",
            telefone="(11) 99999-9999"
        )
        self.assertEqual(departamento.nome, "TI")
        self.assertEqual(departamento.responsavel, "João Silva")
        self.assertEqual(departamento.telefone, "(11) 99999-9999")
        self.assertEqual(str(departamento), "TI")

class FornecedorModelTest(TestCase):
    def test_criar_fornecedor(self):
        """Testa a criação de um fornecedor."""
        fornecedor = Fornecedor.objects.create(
            nome="Fornecedor XYZ",
            cnpj="12.345.678/0001-99",
            telefone="(11) 99999-9999",
            email="contato@fornecedorxyz.com"
        )
        self.assertEqual(fornecedor.nome, "Fornecedor XYZ")
        self.assertEqual(fornecedor.cnpj, "12.345.678/0001-99")
        self.assertEqual(fornecedor.telefone, "(11) 99999-9999")
        self.assertEqual(fornecedor.email, "contato@fornecedorxyz.com")
        self.assertEqual(str(fornecedor), "Fornecedor XYZ")

    def test_cnpj_unico(self):
        """Testa a unicidade do CNPJ."""
        Fornecedor.objects.create(
            nome="Fornecedor A",
            cnpj="12.345.678/0001-99",
            telefone="(11) 99999-9999"
        )
        with self.assertRaises(ValidationError):
            fornecedor = Fornecedor(
                nome="Fornecedor B",
                cnpj="12.345.678/0001-99",
                telefone="(11) 88888-8888"
            )
            fornecedor.full_clean()  # Valida o modelo

class BemModelTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome="Eletrônicos")
        self.departamento = Departamento.objects.create(nome="TI", responsavel="João Silva")
        self.fornecedor = Fornecedor.objects.create(nome="Fornecedor XYZ", cnpj="12.345.678/0001-99")

    def test_criar_bem(self):
        """Testa a criação de um bem."""
        bem = Bem.objects.create(
            nome="Notebook",
            descricao="Notebook Dell",
            categoria=self.categoria,
            departamento=self.departamento,
            fornecedor=self.fornecedor,
            data_aquisicao=date(2023, 1, 1),
            valor=5000.00,
            rfid="1234567890",
            status="ativo"
        )
        self.assertEqual(bem.nome, "Notebook")
        self.assertEqual(bem.descricao, "Notebook Dell")
        self.assertEqual(bem.categoria, self.categoria)
        self.assertEqual(bem.departamento, self.departamento)
        self.assertEqual(bem.fornecedor, self.fornecedor)
        self.assertEqual(bem.data_aquisicao.strftime("%Y-%m-%d"), "2023-01-01")
        self.assertEqual(bem.valor, 5000.00)
        self.assertEqual(bem.rfid, "1234567890")
        self.assertEqual(bem.status, "ativo")
        self.assertEqual(str(bem), "Notebook")