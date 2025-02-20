import os
import django
from datetime import datetime, timedelta
from random import choice, randint
from faker import Faker

# Configura o Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'syspatri.settings')
django.setup()

from patrimonio.models import Categoria, Departamento, Fornecedor, Bem
from controle.models import Movimentacao, Manutencao, Auditoria
from core.models import Usuario

# Inicializa o Faker
fake = Faker('pt_BR')  # Usa localização brasileira

# Função para criar categorias
def criar_categorias():
    categorias = [
        "Eletrônicos", "Móveis", "Equipamentos de Escritório", "Veículos", "Ferramentas",
        "Informática", "Ar Condicionado", "Iluminação", "Segurança", "Limpeza",
        "Cozinha", "Laboratório", "Biblioteca", "Esportes", "Saúde",
        "Manutenção", "Telecomunicações", "Energia", "Áudio e Vídeo", "Outros"
    ]
    for nome in categorias:
        Categoria.objects.create(nome=nome, descricao=fake.text(max_nb_chars=200))

# Função para criar departamentos
def criar_departamentos():
    for _ in range(20):
        Departamento.objects.create(
            nome=fake.company(),
            responsavel=fake.name(),
            telefone=fake.phone_number()
        )

# Função para criar fornecedores
def criar_fornecedores():
    for _ in range(20):
        Fornecedor.objects.create(
            nome=fake.company(),
            cnpj=fake.cnpj(),
            telefone=fake.phone_number(),
            email=fake.company_email()
        )

# Função para criar bens
def criar_bens():
    categorias = Categoria.objects.all()
    departamentos = Departamento.objects.all()
    fornecedores = Fornecedor.objects.all()
    for _ in range(1000):
        Bem.objects.create(
            nome=fake.word().capitalize() + " " + fake.word().capitalize(),
            descricao=fake.text(max_nb_chars=200),
            categoria=choice(categorias),
            departamento=choice(departamentos),
            fornecedor=choice(fornecedores),
            data_aquisicao=fake.date_between(start_date='-5y', end_date='today'),
            valor=randint(100, 10000),
            rfid=fake.uuid4(),
            status=choice(['ativo', 'inativo'])
        )

# Função para criar movimentações
def criar_movimentacoes():
    bens = Bem.objects.all()
    departamentos = Departamento.objects.all()
    usuarios = Usuario.objects.all()
    for _ in range(20):
        Movimentacao.objects.create(
            bem=choice(bens),
            departamento_origem=choice(departamentos),
            departamento_destino=choice(departamentos),
            responsavel=choice(usuarios),
            observacao=fake.text(max_nb_chars=100)
        )

# Função para criar manutenções
def criar_manutencoes():
    bens = Bem.objects.all()
    usuarios = Usuario.objects.all()
    for _ in range(50):
        Manutencao.objects.create(
            bem=choice(bens),
            data_inicio=fake.date_between(start_date='-1y', end_date='today'),
            data_fim=fake.date_between(start_date='today', end_date='+1y') if randint(0, 1) else None,
            responsavel=choice(usuarios),
            custo=randint(100, 1000),
            descricao=fake.text(max_nb_chars=200)
        )

# Função para criar auditorias
def criar_auditorias():
    departamentos = Departamento.objects.all()
    usuarios = Usuario.objects.all()
    for _ in range(20):
        Auditoria.objects.create(
            departamento=choice(departamentos),
            responsavel=choice(usuarios),
            observacao=fake.text(max_nb_chars=200)
        )

# Função para criar usuários
def criar_usuarios():
    for _ in range(20):
        Usuario.objects.create_user(
            username=fake.user_name(),
            email=fake.email(),
            password="senha123",
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            gerente=choice([True, False])
        )

# Executa as funções para popular o banco de dados
if __name__ == "__main__":
    print("Criando categorias...")
    criar_categorias()
    print("Criando departamentos...")
    criar_departamentos()
    print("Criando fornecedores...")
    criar_fornecedores()
    print("Criando usuários...")
    criar_usuarios()
    print("Criando bens...")
    criar_bens()
    print("Criando movimentações...")
    criar_movimentacoes()
    print("Criando manutenções...")
    criar_manutencoes()
    print("Criando auditorias...")
    criar_auditorias()
    print("Banco de dados populado com sucesso!")
    
    