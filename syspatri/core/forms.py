from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'departamento', 'cargo', 'password1', 'password2']

class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'departamento', 'cargo']

class LoginForm(forms.Form):
    username = forms.CharField(label="Usuário", max_length=100)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)