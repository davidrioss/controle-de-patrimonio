from django.urls import path
from . import views

urlpatterns = [
    path('bens/', views.listar_bens, name='listar_bens'),
    path('bens/adicionar/', views.adicionar_bem, name='adicionar_bem'),
    path('bens/editar/<int:pk>/', views.atualizar_bem, name='atualizar_bem'),
    path('bens/detalhes/<int:pk>/', views.detalhes_bem, name='detalhes_bem'),
    path('bens/excluir/<int:pk>/', views.excluir_bem, name='excluir_bem'),

    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/adicionar/', views.adicionar_categoria, name='adicionar_categoria'),
    path('categorias/editar/<int:pk>/', views.atualizar_categoria, name='atualizar_categoria'),
    path('categorias/detalhes/<int:pk>/', views.detalhes_categoria, name='detalhes_categoria'),
    path('categorias/excluir/<int:pk>/', views.excluir_categoria, name='excluir_categoria'),

    path('departamentos/', views.listar_departamentos, name='listar_departamentos'),
    path('departamentos/adicionar/', views.adicionar_departamento, name='adicionar_departamento'),
    path('departamentos/editar/<int:pk>/', views.atualizar_departamento, name='atualizar_departamento'),
    path('departamentos/detalhes/<int:pk>/', views.detalhes_departamento, name='detalhes_departamento'),
    path('departamentos/excluir/<int:pk>/', views.excluir_departamento, name='excluir_departamento'),

    path('fornecedores/', views.listar_fornecedores, name='listar_fornecedores'),
    path('fornecedores/adicionar/', views.adicionar_fornecedor, name='adicionar_fornecedor'),
    path('fornecedores/editar/<int:pk>/', views.atualizar_fornecedor, name='atualizar_fornecedor'),
    path('fornecedores/detalhes/<int:pk>/', views.detalhes_fornecedor, name='detalhes_fornecedor'),
    path('fornecedores/excluir/<int:pk>/', views.excluir_fornecedor, name='excluir_fornecedor'),
]