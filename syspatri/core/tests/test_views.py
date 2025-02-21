from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from patrimonio.models import Departamento, Bem, Categoria
from controle.models import Manutencao

User = get_user_model()

class DashboardViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123"
        )
        self.departamento = Departamento.objects.create(nome="TI")
        self.categoria = Categoria.objects.create(nome="Eletrônicos", descricao="Categoria de eletrônicos")
        self.bem = Bem.objects.create(
            nome="Notebook",
            descricao="Notebook Dell",
            departamento=self.departamento,
            categoria=self.categoria,
            valor=5000.00,
            data_aquisicao="2021-01-01",
            rfid="RFID123",
        )
        self.manutencao = Manutencao.objects.create(
            bem=self.bem,
            descricao="Manutenção preventiva",
            custo=200.00,
            data_inicio="2021-01-15",
        )

    def test_dashboard_authenticated(self):
        """Testa o acesso à dashboard por um usuário autenticado."""
        self.client.login(username="testuser", password="testpassword123")
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')
        self.assertIn('total_bens', response.context)
        self.assertIn('total_departamentos', response.context)
        self.assertIn('valor_total_patrimonio', response.context)

    def test_dashboard_unauthenticated(self):
        """Testa o acesso à dashboard por um usuário não autenticado."""
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)  # Redireciona para o login
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('dashboard')}")
        
class UsuarioViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123"
        )
        self.admin_user = User.objects.create_user(
            username="admin",
            password="adminpassword123",
            gerente=True
        )
        self.departamento = Departamento.objects.create(nome="TI")

    def test_listar_usuarios_authenticated(self):
        """Testa o acesso à lista de usuários por um administrador."""
        self.client.login(username="admin", password="adminpassword123")
        response = self.client.get(reverse('listar_usuarios'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listar_usuarios.html')

    def test_listar_usuarios_unauthenticated(self):
        """Testa o acesso à lista de usuários por um usuário não autenticado."""
        response = self.client.get(reverse('listar_usuarios'))
        self.assertEqual(response.status_code, 302)  # Redireciona para o login
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('listar_usuarios')}")

    def test_listar_usuarios_common_user(self):
        """Testa o acesso à lista de usuários por um usuário comum."""
        self.client.login(username="testuser", password="testpassword123")
        response = self.client.get(reverse('listar_usuarios'))
        self.assertEqual(response.status_code, 302)  # Acesso proibido

    def test_adicionar_usuario_authenticated(self):
        """Testa a adição de um novo usuário por um administrador."""
        self.client.login(username="admin", password="adminpassword123")
        form_data = {
            'username': 'newuser',
            'first_name': 'New',
            'last_name': 'User',
            'email': 'newuser@example.com',
            'departamento': self.departamento.id,
            'cargo': 'Analista',
            'gerente': False,
            'password1': 'newpassword123',
            'password2': 'newpassword123',
        }
        response = self.client.post(reverse('adicionar_usuario'), data=form_data)
        self.assertEqual(response.status_code, 302)  # Redireciona após criação
        self.assertRedirects(response, reverse('listar_usuarios'))
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_atualizar_usuario_authenticated(self):
        """Testa a atualização de um usuário por um administrador."""
        self.client.login(username="admin", password="adminpassword123")
        usuario = User.objects.create_user(
            username="usuario_teste",
            password="testpassword123"
        )
        form_data = {
            'username': 'usuario_teste',
            'first_name': 'Updated',
            'last_name': 'User',
            'email': 'updated@example.com',
            'departamento': self.departamento.id,
            'cargo': 'Gerente',
            'gerente': True,
            'password': 'newpassword123',
        }
        response = self.client.post(reverse('atualizar_usuario', args=[usuario.pk]), data=form_data)
        self.assertEqual(response.status_code, 302)  # Redireciona após atualização
        self.assertRedirects(response, reverse('listar_usuarios'))
        usuario.refresh_from_db()
        self.assertEqual(usuario.first_name, 'Updated')

    def test_excluir_usuario_authenticated(self):
        """Testa a exclusão de um usuário por um administrador."""
        self.client.login(username="admin", password="adminpassword123")
        usuario = User.objects.create_user(
            username="usuario_teste",
            password="testpassword123"
        )
        response = self.client.post(reverse('excluir_usuario', args=[usuario.pk]))
        self.assertEqual(response.status_code, 302)  # Redireciona após exclusão
        self.assertRedirects(response, reverse('listar_usuarios'))
        self.assertFalse(User.objects.filter(username='usuario_teste').exists())
        
class AutenticacaoViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123"
        )

    def test_custom_login_valid(self):
        """Testa o login com credenciais válidas."""
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword123',
        })
        self.assertEqual(response.status_code, 302)  # Redireciona para a dashboard
        self.assertRedirects(response, reverse('dashboard'))

    def test_custom_login_invalid(self):
        """Testa o login com credenciais inválidas."""
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, 200)  # Permanece na página de login
        self.assertContains(response, "Usuário ou senha incorretos.")

    def test_custom_logout(self):
        """Testa o logout de um usuário autenticado."""
        self.client.login(username="testuser", password="testpassword123")
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redireciona para o login
        self.assertRedirects(response, reverse('login'))

    def test_perfil_usuario_authenticated(self):
        """Testa o acesso ao perfil do usuário autenticado."""
        self.client.login(username="testuser", password="testpassword123")
        response = self.client.get(reverse('perfil_usuario'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'perfil.html')

    def test_perfil_usuario_unauthenticated(self):
        """Testa o acesso ao perfil do usuário não autenticado."""
        response = self.client.get(reverse('perfil_usuario'))
        self.assertEqual(response.status_code, 302)  # Redireciona para o login
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('perfil_usuario')}")