from django.test import TestCase
from django.contrib.auth import get_user_model
from patrimonio.models import Departamento

User = get_user_model()

class UsuarioModelTest(TestCase):
    def setUp(self):
        # Cria um departamento para teste
        self.departamento = Departamento.objects.create(nome="TI")
        
        # Cria um usuário para teste
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

    def test_usuario_creation(self):
        """Testa a criação de um usuário."""
        self.assertEqual(self.usuario.username, "testuser")
        self.assertEqual(self.usuario.first_name, "Test")
        self.assertEqual(self.usuario.last_name, "User")
        self.assertEqual(self.usuario.email, "test@example.com")
        self.assertEqual(self.usuario.departamento, self.departamento)
        self.assertEqual(self.usuario.cargo, "Analista")
        self.assertTrue(self.usuario.gerente)
        self.assertTrue(self.usuario.check_password("testpassword123"))

    def test_usuario_str(self):
        """Testa o método __str__ do modelo Usuario."""
        self.assertEqual(str(self.usuario), "Test User")