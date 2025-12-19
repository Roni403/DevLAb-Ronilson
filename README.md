md
# Projeto Integrador – Sistema de Gestão de Eventos

## Descrição do Projeto
Este projeto consiste no desenvolvimento de uma **API Backend para Gestão de Eventos**, criada como parte do Projeto Integrador do curso.  
O sistema tem como objetivo centralizar e organizar informações relacionadas a eventos acadêmicos e corporativos, como congressos, conferências, semanas acadêmicas e feiras.

A aplicação permite o gerenciamento de:
- Eventos
- Participantes
- Atividades (palestras, workshops, oficinas)
- Relacionamentos entre essas entidades

A solução evita o uso de planilhas e formulários dispersos, garantindo maior controle, integridade dos dados e facilidade de gestão.

---

## Objetivo Geral
Desenvolver uma **API Backend com autenticação**, capaz de realizar operações completas de cadastro, consulta, atualização e exclusão (CRUD) das entidades do sistema, além de disponibilizar rotas que evidenciem os relacionamentos entre eventos, participantes e atividades.

---

## Escopo do Sistema

### Entidades Principais

**Evento**
- nome
- descrição
- data_início
- data_fim
- local

**Participante**
- nome
- email
- celular
- tipo (estudante, convidado, palestrante, etc.)

**Atividade**
- título
- descrição
- horário_início
- horário_fim
- tipo (workshop, palestra, oficina, etc.)

---

## Relacionamentos

- **1:N — Evento para Atividade**  
  Um evento pode possuir várias atividades, enquanto cada atividade pertence a apenas um evento.

- **N:N — Evento com Participante**  
  Um participante pode se inscrever em vários eventos, e um evento pode possuir vários participantes.

- **1:1 (ou 1:N) — Atividade com Participante (Responsável)**  
  Cada atividade possui um participante responsável, como um palestrante ou facilitador.

---

## Funcionalidades da API

### Rotas CRUD (todas as entidades)
- GET – Listar e detalhar registros
- POST – Criar registros
- PUT / PATCH – Atualizar registros
- DELETE – Remover registros

---

### Rotas de Relacionamento

**Participantes de um Evento (N:N)**
- `GET /eventos/{id}/participantes`
- `POST /eventos/{id}/participantes`

**Atividades de um Evento (1:N)**
- `GET /eventos/{id}/atividades`
- `POST /eventos/{id}/atividades`

**Responsável por Atividade**
- `GET /atividades/{id}/responsavel`
- `PUT /atividades/{id}/responsavel`

---

### Rota Composta (A-B-C)
- `GET /eventos/{id}/dashboard`

Retorna:
- Dados do evento
- Lista de atividades
- Responsável por cada atividade
- Lista de participantes do evento

---

## Autenticação

O sistema implementa autenticação para controle de acesso às rotas sensíveis.

### Rotas Protegidas
- Criar, editar e deletar eventos
- Criar, editar e deletar atividades
- Definir responsável por atividade
- Inscrever participantes em eventos

### Rotas Públicas
- Listagem de eventos
- Listagem de atividades

---

## Tecnologias Utilizadas
- Python 3
- Django
- Django Rest Framework
- SQLite (ambiente de desenvolvimento)

---

## Instalação e Execução

### 1. Clonar o repositório
```bash
git clone https://github.com/Roni403/DevLAb-Ronilson.git
cd DevLAb-Ronilson

---

## 👨‍💻 Contribuição – Eduardo Neves

### Alterações realizadas no README
- Padronização visual e textual (remoção de emojis, substituição de símbolos → por termos textuais)
- Organização das seções de instalação, execução e informações do projeto
- Revisão geral do Markdown para melhor legibilidade

📅 Dezembro/2025

---

# Projeto DevLAb-Ronilson

Este repositório contém o projeto Django desenvolvido como trabalho para avaliação.

### Informações importantes
- Servidor de desenvolvimento: http://127.0.0.1:8000/
- Superusuário criado para acessar o admin: `csantos`
- Commit de teste incluído para garantir que a entrega seja visível no repositório

### Como rodar o projeto
1. Ative o ambiente virtual:
   ```bash
   source sistem/Scripts/activate   # Git Bash
   .\sistem\Scripts\Activate.ps1    # PowerShell
