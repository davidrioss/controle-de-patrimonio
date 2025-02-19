from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        

class Departamento(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    responsavel = models.CharField(max_length=100, verbose_name="Responsável")
    telefone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefone")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"


class Fornecedor(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    cnpj = models.CharField(max_length=18, unique=True, verbose_name="CNPJ")
    telefone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefone")
    email = models.EmailField(blank=True, null=True, verbose_name="E-mail")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"


class Bem(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, verbose_name="Categoria")
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, verbose_name="Departamento")
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True, verbose_name="Fornecedor")
    data_aquisicao = models.DateField(verbose_name="Data de Aquisição")
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    rfid = models.CharField(max_length=50, unique=True, verbose_name="RFID")
    status = models.CharField(max_length=20, choices=[('ativo', 'Ativo'), ('inativo', 'Inativo')], default='ativo', verbose_name="Status")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Bem"
        verbose_name_plural = "Bens"















