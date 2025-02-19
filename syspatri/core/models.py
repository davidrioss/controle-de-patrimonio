from django.contrib.auth.models import AbstractUser
from django.db import models
from patrimonio.models import Departamento  # Importando Departamento de patrimonio

class Usuario(AbstractUser):
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Departamento")
    cargo = models.CharField(max_length=100, blank=True, null=True, verbose_name="Cargo")

    # Adicione related_name único para evitar conflitos
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="usuario_groups",  # Nome único para o related_name
        related_query_name="usuario",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="usuario_permissions",  # Nome único para o related_name
        related_query_name="usuario",
    )

    def __str__(self):
        return self.get_full_name() or self.username