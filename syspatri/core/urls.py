from django.urls import path
from . import views

urlpatterns = [
    # Página inicial (Dashboard)
    path('', views.dashboard, name='dashboard'),

    # Autenticação
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),

    # Registro de usuários
    path('registro/', views.registro, name='registro'),

    # Perfil do usuário
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),

    # Gerenciamento de usuários (apenas para administradores)
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/adicionar/', views.adicionar_usuario, name='adicionar_usuario'),
    path('usuarios/editar/<int:pk>/', views.atualizar_usuario, name='atualizar_usuario'),
    path('usuarios/detalhes/<int:pk>/', views.detalhes_usuario, name='detalhes_usuario'),
    path('usuarios/excluir/<int:pk>/', views.excluir_usuario, name='excluir_usuario'),
]