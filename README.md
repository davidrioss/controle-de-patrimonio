# SYSPATRI - Sistema de Gestão de Patrimônio

Este é um sistema de gestão de patrimônio desenvolvido em Django para gerenciar bens, categorias, departamentos e fornecedores. O sistema permite o cadastro, edição, exclusão e visualização de informações relacionadas ao patrimônio de uma organização.

## Funcionalidades

- **Gestão de Bens**: Cadastro, edição, exclusão e visualização de bens patrimoniais.
- **Gestão de Categorias**: Organização dos bens em categorias.
- **Gestão de Departamentos**: Associação de bens a departamentos.
- **Gestão de Fornecedores**: Cadastro de fornecedores dos bens.
- **Dashboard**: Visualização de métricas e gráficos relacionados ao patrimônio.
- **Autenticação e Autorização**: Controle de acesso com autenticação de usuários e permissões.
- **Registro de auditorias, movimentações e manutenções.**

## Tecnologias Utilizadas

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Banco de Dados**: SQLite (padrão do Django)
- **Ferramentas**: Chart.js (gráficos)


## Estrutura do Projeto
- core/: Aplicação principal para autenticação, usuários e dashboard.

- patrimonio/: Aplicação para gestão de bens, categorias, departamentos e fornecedores.

- controle/: Aplicação para gestão de movimentações, manutenções e auditorias.

