from django.test import TestCase
from django.contrib.auth import get_user_model
from patrimonio.models import Departamento
from core.forms import UsuarioCreationForm, UsuarioChangeForm

User = get_user_model()

class UsuarioCreationFormTest(TestCase):
    def setUp(self):
        self.departamento = Departamento.objects.create(nome="TI")

    def test_usuario_creation_form_valid(self):
        """Testa se o formulário de criação de usuário é válido com dados corretos."""
        form_data = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'departamento': self.departamento.id,
            'cargo': 'Analista',
            'gerente': True,
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        form = UsuarioCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_usuario_creation_form_invalid(self):
        """Testa se o formulário de criação de usuário é inválido com dados incorretos."""
        form_data = {
            'username': '',  # Campo obrigatório
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'invalid-email',  # Email inválido
            'departamento': self.departamento.id,
            'cargo': 'Analista',
            'gerente': True,
            'password1': 'testpassword123',
            'password2': 'differentpassword',  # Senhas não coincidem
        }
        form = UsuarioCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('password2', form.errors)

class UsuarioChangeFormTest(TestCase):
    def setUp(self):
        self.departamento = Departamento.objects.create(nome="TI")
        self.usuario = User.objects.create_user(
            username="testuser",
            first_name="Test",
            last_name="User",
            email="test@example.com",
            departamento=self.departamento,
            cargo="Analista",
            gerente=True,
            password="testpassword123"
        )

    def test_usuario_change_form_valid(self):
        """Testa se o formulário de edição de usuário é válido com dados corretos."""
        form_data = {
            'username': 'testuser',
            'first_name': 'Updated',
            'last_name': 'User',
            'email': 'updated@example.com',
            'departamento': self.departamento.id,
            'cargo': 'Gerente',
            'gerente': False,
            'password': 'newpassword123',  # Nova senha
        }
        form = UsuarioChangeForm(data=form_data, instance=self.usuario)
        self.assertTrue(form.is_valid())

    def test_usuario_change_form_invalid(self):
        """Testa se o formulário de edição de usuário é inválido com dados incorretos."""
        form_data = {
            'username': '',  # Campo obrigatório
            'first_name': 'Updated',
            'last_name': 'User',
            'email': 'invalid-email',  # Email inválido
            'departamento': self.departamento.id,
            'cargo': 'Gerente',
            'gerente': False,
            'password': 'newpassword123',
        }
        form = UsuarioChangeForm(data=form_data, instance=self.usuario)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('email', form.errors)