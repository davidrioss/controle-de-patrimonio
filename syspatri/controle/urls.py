from django.urls import path
from . import views

urlpatterns = [
    # Movimentações
    path('movimentacoes/', views.listar_movimentacoes, name='listar_movimentacoes'),
    path('movimentacoes/adicionar/', views.adicionar_movimentacao, name='adicionar_movimentacao'),
    path('movimentacoes/editar/<int:pk>/', views.atualizar_movimentacao, name='atualizar_movimentacao'),
    path('movimentacoes/detalhes/<int:pk>/', views.detalhes_movimentacao, name='detalhes_movimentacao'),
    path('movimentacoes/excluir/<int:pk>/', views.excluir_movimentacao, name='excluir_movimentacao'),

    # Manutenções
    path('manutencoes/', views.listar_manutencoes, name='listar_manutencoes'),
    path('manutencoes/adicionar/', views.adicionar_manutencao, name='adicionar_manutencao'),
    path('manutencoes/editar/<int:pk>/', views.atualizar_manutencao, name='atualizar_manutencao'),
    path('manutencoes/detalhes/<int:pk>/', views.detalhes_manutencao, name='detalhes_manutencao'),
    path('manutencoes/excluir/<int:pk>/', views.excluir_manutencao, name='excluir_manutencao'),

    # Auditorias
    path('auditorias/', views.listar_auditorias, name='listar_auditorias'),
    path('auditorias/adicionar/', views.adicionar_auditoria, name='adicionar_auditoria'),
    path('auditorias/editar/<int:pk>/', views.atualizar_auditoria, name='atualizar_auditoria'),
    path('auditorias/detalhes/<int:pk>/', views.detalhes_auditoria, name='detalhes_auditoria'),
    path('auditorias/excluir/<int:pk>/', views.excluir_auditoria, name='excluir_auditoria'),
]
