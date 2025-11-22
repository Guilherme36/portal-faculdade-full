# Sistema Gerenciador de Turmas

## 👥 Integrantes do Grupo

- **Guilherme** - RA: [211590]
- **[Nome do Integrante 2]** - RA: [RA]
- **[Nome do Integrante 3]** - RA: [RA]

## 📋 Resumo do Projeto

Sistema completo de gerenciamento de turmas acadêmicas desenvolvido com arquitetura de microserviços, demonstrando conceitos avançados de programação distribuída.

### O que é?

Uma aplicação web que permite gerenciar:
- **Alunos** - Cadastro, edição e exclusão
- **Professores** - Gerenciamento completo
- **Matérias** - Controle de disciplinas
- **Turmas** - Criação e gestão de turmas com horários
- **Inscrições** - Matrícula de alunos em turmas

### Como funciona?

O sistema utiliza arquitetura de microserviços:

```
Cliente Web → Frontend (Django REST) → Backend (gRPC) → SQLite
                                            ↓
                                        RabbitMQ
                                            ↓
                                        Consumer
```

- **Frontend**: API REST em Django que serve interface web e endpoints JSON
- **Backend**: Servidor gRPC com lógica de negócio e persistência
- **RabbitMQ**: Sistema de mensagens para processamento assíncrono de inscrições
- **SQLite**: Banco de dados local

### Tecnologias Utilizadas

- **Python 3.11**
- **Django 4.2** + Django REST Framework
- **gRPC** + Protocol Buffers
- **RabbitMQ** (AMQP)
- **SQLAlchemy** (ORM)
- **pandas/numpy** (processamento vetorizado)
- **Docker**

## 🚀 Como Executar do Zero

### Pré-requisitos

- Python 3.9+
- Docker
- Git

### Passo a Passo Completo

#### 1. Clonar/Extrair o Projeto

```bash
cd AF
```

#### 2. Executar Setup Inicial

```bash
setup_local.bat
```

Este script faz tudo automaticamente:
- Cria ambiente virtual
- Instala todas as dependências (backend e frontend)
- Compila os arquivos Protocol Buffers
- Cria o banco de dados

#### 3. Iniciar RabbitMQ

```bash
docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

#### 4. Iniciar Backend (Terminal 1)

```bash
start_backend.bat
```

#### 5. Iniciar Frontend (Terminal 2)

```bash
start_frontend.bat
```

#### 6. Acessar o Sistema

Abra o navegador em: **http://localhost:8000**


## 📖 Exemplo de Uso

### Interface Web

1. Acesse http://localhost:8000
2. Navegue pelos menus: Alunos, Professores, Matérias, Turmas
3. Use os formulários para criar registros
4. Clique em "Editar" para modificar (abre modal)
5. Clique em "Deletar" para remover

### API REST

#### Criar Aluno
```bash
curl -X POST http://localhost:8000/api/alunos/ \
  -H "Content-Type: application/json" \
  -d '{"nome": "João Silva", "email": "joao@email.com", "matricula": "2024001"}'
```

#### Listar Alunos
```bash
curl http://localhost:8000/api/alunos/
```

#### Criar Professor
```bash
curl -X POST http://localhost:8000/api/professores/ \
  -H "Content-Type: application/json" \
  -d '{"nome": "Maria Santos", "email": "maria@email.com", "area": "Computação"}'
```

#### Criar Matéria
```bash
curl -X POST http://localhost:8000/api/materias/ \
  -H "Content-Type: application/json" \
  -d '{"nome": "Programação Distribuída", "descricao": "Sistemas distribuídos", "carga_horaria": 80}'
```

#### Criar Turma
```bash
curl -X POST http://localhost:8000/api/turmas/ \
  -H "Content-Type: application/json" \
  -d '{"materia_id": 1, "professor_id": 1, "dia_semana": "Segunda", "hora_inicio": "19:00", "hora_fim": "21:00"}'
```

#### Inscrever Aluno em Turma
```bash
curl -X POST http://localhost:8000/api/turmas/1/inscricoes/ \
  -H "Content-Type: application/json" \
  -d '{"aluno_id": 1}'
```

#### Obter Relatório (com processamento vetorizado)
```bash
curl http://localhost:8000/api/relatorios/turmas/
```

## 🧪 Executar Testes

```bash
# Testes de integração
python test_endpoints_clean.py

# Testes unitários do backend
cd backend_service
python -m pytest tests/

# Testes unitários do frontend
cd frontend_service
python manage.py test
```

## 🎯 Funcionalidades Implementadas

✅ CRUD completo de Alunos, Professores, Matérias e Turmas  
✅ Interface web com modais para edição  
✅ API REST JSON  
✅ Comunicação gRPC entre frontend e backend  
✅ Sistema de mensagens AMQP com RabbitMQ  
✅ Validação de conflito de horários  
✅ Prevenção de inscrição duplicada  
✅ Relatórios com processamento vetorizado (pandas/numpy)  
✅ Deleção em cascata de relacionamentos  
✅ Testes automatizados  

## 📂 Estrutura do Projeto

```
AF/
├── backend_service/          # Servidor gRPC
│   ├── protos/              # Protocol Buffers
│   ├── tests/               # Testes unitários
│   ├── server.py            # Servidor gRPC
│   ├── services.py          # Lógica de negócio
│   ├── database.py          # Modelos SQLAlchemy
│   ├── message_queue.py     # Publicador RabbitMQ
│   └── consumer.py          # Consumidor AMQP
├── frontend_service/         # Django REST API
│   ├── api/
│   │   ├── templates/       # Interface web HTML
│   │   ├── views.py         # API REST
│   │   └── grpc_client.py   # Cliente gRPC
│   └── turmas_api/          # Configuração Django
├── setup_local.bat           # Setup inicial completo
├── start_backend.bat         # Inicia backend
├── start_frontend.bat        # Inicia frontend
├── test_endpoints_clean.py   # Testes de integração
└── README.md                 # Este arquivo
```

## 🌐 Endpoints Disponíveis

- **Frontend Web**: http://localhost:8000
- **Backend gRPC**: localhost:50051
- **RabbitMQ Management**: http://localhost:15672 (guest/guest)

## 📊 Conceitos de Programação Distribuída

1. **gRPC** - Comunicação eficiente entre serviços com Protocol Buffers
2. **REST API** - Interface JSON para clientes web
3. **AMQP** - Mensageria assíncrona com RabbitMQ
4. **Microserviços** - Separação de responsabilidades
5. **Processamento Vetorizado** - pandas/numpy para análise de dados
6. **ORM** - Abstração de banco de dados com SQLAlchemy

---

**Desenvolvido para:** Facens - Programação Distribuída  
**Ano:** 2025
