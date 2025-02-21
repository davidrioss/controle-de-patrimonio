from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class CoreURLsTest(TestCase):
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

    def test_dashboard_url(self):
        """Testa o acesso à URL da dashboard."""
        url = reverse('dashboard')
        # Usuário não autenticado é redirecionado para o login
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('login')}?next={url}")

        # Usuário autenticado pode acessar
        self.client.login(username="testuser", password="testpassword123")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_login_url(self):
        """Testa o acesso à URL de login."""
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_logout_url(self):
        """Testa o acesso à URL de logout."""
        url = reverse('logout')
        # Usuário autenticado é redirecionado para o login após logout
        self.client.login(username="testuser", password="testpassword123")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

    def test_perfil_usuario_url(self):
        """Testa o acesso à URL do perfil do usuário."""
        url = reverse('perfil_usuario')
        # Usuário não autenticado é redirecionado para o login
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('login')}?next={url}")

        # Usuário autenticado pode acessar
        self.client.login(username="testuser", password="testpassword123")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_listar_usuarios_url(self):
        """Testa o acesso à URL de listar usuários."""
        url = reverse('listar_usuarios')
        # Usuário não autenticado é redirecionado para o login
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('login')}?next={url}")

        # Usuário comum não tem permissão
        self.client.login(username="testuser", password="testpassword123")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Proibido

        # Administrador ou gerente pode acessar
        self.client.login(username="admin", password="adminpassword123")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_adicionar_usuario_url(self):
        """Testa o acesso à URL de adicionar usuário."""
        url = reverse('adicionar_usuario')
        # Usuário não autenticado é redirecionado para o login
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('login')}?next={url}")

        # Usuário comum não tem permissão
        self.client.login(username="testuser", password="testpassword123")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Proibido

        # Administrador ou gerente pode acessar
        self.client.login(username="admin", password="adminpassword123")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_atualizar_usuario_url(self):
        """Testa o acesso à URL de atualizar usuário."""
        usuario = User.objects.create_user(
            username="usuario_teste",
            password="testpassword123"
        )
        url = reverse('atualizar_usuario', args=[usuario.pk])
        # Usuário não autenticado é redirecionado para o login
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('login')}?next={url}")

        # Usuário comum não tem permissão
        self.client.login(username="testuser", password="testpassword123")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Proibido

        # Administrador ou gerente pode acessar
        self.client.login(username="admin", password="adminpassword123")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detalhes_usuario_url(self):
        """Testa o acesso à URL de detalhes do usuário."""
        usuario = User.objects.create_user(
            username="usuario_teste",
            password="testpassword123"
        )
        url = reverse('detalhes_usuario', args=[usuario.pk])
        # Usuário não autenticado é redirecionado para o login
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('login')}?next={url}")

        # Usuário comum não tem permissão
        self.client.login(username="testuser", password="testpassword123")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Proibido

        # Administrador ou gerente pode acessar
        self.client.login(username="admin", password="adminpassword123")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_excluir_usuario_url(self):
        """Testa o acesso à URL de excluir usuário."""
        usuario = User.objects.create_user(
            username="usuario_teste",
            password="testpassword123"
        )
        url = reverse('excluir_usuario', args=[usuario.pk])
        # Usuário não autenticado é redirecionado para o login
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"{reverse('login')}?next={url}")

        # Usuário comum não tem permissão
        self.client.login(username="testuser", password="testpassword123")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Proibido

        # Administrador ou gerente pode acessar
        self.client.login(username="admin", password="adminpassword123")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Redireciona após exclusão
        self.assertRedirects(response, reverse('listar_usuarios'))