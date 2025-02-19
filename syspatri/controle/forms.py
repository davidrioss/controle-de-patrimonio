from django import forms
from .models import Movimentacao, Manutencao, Auditoria
from patrimonio.models import Bem, Departamento
from core.models import Usuario

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = ['bem', 'departamento_origem', 'departamento_destino', 'responsavel', 'observacao']
        widgets = {
            'observacao': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtra os bens ativos
        self.fields['bem'].queryset = Bem.objects.filter(status='ativo')

class ManutencaoForm(forms.ModelForm):
    class Meta:
        model = Manutencao
        fields = ['bem', 'data_inicio', 'data_fim', 'responsavel', 'custo', 'descricao']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
            'descricao': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtra os bens ativos
        self.fields['bem'].queryset = Bem.objects.filter(status='ativo')

class AuditoriaForm(forms.ModelForm):
    class Meta:
        model = Auditoria
        fields = ['bem', 'responsavel', 'observacao']
        widgets = {
            'observacao': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtra os bens ativos
        self.fields['bem'].queryset = Bem.objects.filter(status='ativo')