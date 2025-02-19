from django.db import models
from patrimonio.models import Bem, Departamento
from core.models import Usuario

class Movimentacao(models.Model):
    bem = models.ForeignKey(Bem, on_delete=models.CASCADE, verbose_name="Bem")
    departamento_origem = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name="movimentacoes_origem", verbose_name="Departamento de Origem")
    departamento_destino = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name="movimentacoes_destino", verbose_name="Departamento de Destino")
    data_movimentacao = models.DateTimeField(auto_now_add=True, verbose_name="Data da Movimentação")
    responsavel = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, verbose_name="Responsável")
    observacao = models.TextField(blank=True, null=True, verbose_name="Observação")

    def __str__(self):
        return f"Movimentação de {self.bem.nome}"

    class Meta:
        verbose_name = "Movimentação"
        verbose_name_plural = "Movimentações"


class Manutencao(models.Model):
    bem = models.ForeignKey(Bem, on_delete=models.CASCADE, verbose_name="Bem")
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_fim = models.DateField(blank=True, null=True, verbose_name="Data de Término")
    responsavel = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, verbose_name="Responsável")
    custo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Custo")
    descricao = models.TextField(verbose_name="Descrição")

    def __str__(self):
        return f"Manutenção de {self.bem.nome}"

    class Meta:
        verbose_name = "Manutenção"
        verbose_name_plural = "Manutenções"


class Auditoria(models.Model):
    bem = models.ForeignKey(Bem, on_delete=models.CASCADE, verbose_name="Bem")
    data = models.DateField(auto_now_add=True, verbose_name="Data da Auditoria")
    responsavel = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, verbose_name="Responsável")
    observacao = models.TextField(verbose_name="Observação")

    def __str__(self):
        return f"Auditoria de {self.bem.nome} em {self.data}"

    class Meta:
        verbose_name = "Auditoria"
        verbose_name_plural = "Auditorias"
















