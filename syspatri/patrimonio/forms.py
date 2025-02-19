from django import forms
from .models import Bem, Categoria, Departamento, Fornecedor

class BemForm(forms.ModelForm):
    class Meta:
        model = Bem
        fields = ['nome', 'descricao', 'categoria', 'departamento', 'fornecedor', 'data_aquisicao', 'valor', 'rfid', 'status']
        widgets = {
            'data_aquisicao': forms.DateInput(attrs={'type': 'date'}),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao']

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nome', 'responsavel', 'telefone']

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome', 'cnpj', 'telefone', 'email']