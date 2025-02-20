from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Página inicial (Dashboard)
    path('', views.dashboard, name='dashboard'),

    # Autenticação
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),

    # Perfil do usuário
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),

    # Gerenciamento de usuários (apenas para administradores)
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/adicionar/', views.adicionar_usuario, name='adicionar_usuario'),
    path('usuarios/editar/<int:pk>/', views.atualizar_usuario, name='atualizar_usuario'),
    path('usuarios/detalhes/<int:pk>/', views.detalhes_usuario, name='detalhes_usuario'),
    path('usuarios/excluir/<int:pk>/', views.excluir_usuario, name='excluir_usuario'),
    
    # Redefinição de senha
    path('redefinir-senha/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('redefinir-senha/enviado/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('redefinir-senha/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('redefinir-senha/concluido/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]