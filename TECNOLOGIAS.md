# 🛠️ Documentação de Tecnologias - FilaZero+

## Visão Geral
Este documento descreve todas as tecnologias e dependências utilizadas no projeto **FilaZero+** - Plataforma de Monitoramento de Lotação Hospitalar.

---

## 📋 Backend

### Framework Principal
- **Django 5.2.3**
  - Framework web em Python para desenvolvimento rápido
  - Inclui ORM, admin interface, autenticação e autorização
  - Gerenciamento de rotas e middlewares

### Dependências de Suporte
- **asgiref 3.11.1**
  - Interface assíncrona para servidores ASGI
  - Suporte a WebSockets e processamento assíncrono

- **sqlparse 0.5.5**
  - Parser de SQL para manipulação e formatação de queries
  - Usado internamente pelo Django

- **tzdata 2025.3**
  - Banco de dados de zonas de tempo
  - Essencial para manipulação correta de datas e horários

### Gerenciamento de Configurações
- **django-environ 0.12.0**
  - Carregamento de variáveis de ambiente via arquivo `.env`
  - Separação segura de configurações sensíveis

- **python-dotenv**
  - Alternativa para carregar arquivos `.env` em ambiente Python
  - Facilita configuração local sem hardcoding de credenciais

---

## 🗄️ Banco de Dados

### Drivers de Banco de Dados
- **MySQL**
  - Banco de dados relacional principal
  - Armazena informações de unidades de saúde, pacientes e filas

- **mysql-connector-python**
  - Driver oficial de conexão MySQL para Python
  - Implementa protocolo MySQL nativo

- **mysqlclient**
  - Adaptador Django nativo para MySQL
  - Oferece melhor performance que mysql-connector-python

### Migrations Django
- Sistema de versionamento de schema do banco de dados
- Arquivos em `core_app/migrations/`
- Histórico completo de alterações estruturais

---

## 🎨 Frontend

### Linguagens
- **HTML5**
  - Estruturação semântica das páginas
  - Templates Django em `templates/` e `core_app/templates/`

- **CSS3**
  - Estilização responsiva
  - Arquivos em:
    - `static/css/style.css`
    - `core_app/static/css/style.css`

- **JavaScript (ES6+)**
  - Interatividade e validações no cliente
  - Scripts em:
    - `static/js/script.js`
    - `static/js/format_cpf.js`
    - `core_app/static/js/script.js`

### Funcionalidades Frontend
- Formatação de CPF em tempo real
- Validações de entrada
- Interatividade com o usuário

---

## 🧪 Testes

### Framework de Testes
- **pytest**
  - Framework de testes moderno para Python
  - Configurado em `pytest.ini`
  - Suites de testes em `core_app/test/`

### Tipos de Testes Implementados
- **Testes de Banco de Dados** (`test_db.py`)
  - Validação de modelos e persistência

- **Testes de CPF** (`test_cpf_db.py`)
  - Validação de formato e regras de CPF

- **Testes de Rotas** (`test_rotas.py`)
  - Validação de endpoints HTTP
  - Testes de views

---

## 🔧 Ferramentas de Desenvolvimento

### Gerenciamento de Dependências
- **pip**
  - Gerenciador de pacotes Python
  - Arquivo de dependências: `requirements.txt`

### Scripts de Automação
- **manage.py**
  - Ferramenta CLI do Django para gerenciamento do projeto
  - Comandos: migrate, runserver, createsuperuser, etc.

- **init_db.py**
  - Inicialização e setup do banco de dados
  - Criação de tabelas e dados iniciais

- **seed_db.py** (Management Command)
  - População de dados de teste no banco
  - Localizado em `core_app/management/commands/`

- **INSTALL.bat**
  - Script de instalação rápida para Windows
  - Automatiza setup de ambiente virtual e dependências

---

## 📐 Arquitetura Tecnológica

### Padrão MVC/MVT
```
Django MVT (Model-View-Template):
├── Models (core_app/models.py) - Definição de dados
├── Views (core_app/views.py) - Lógica de negócio
├── Templates (templates/) - Apresentação
└── URLs (core_app/urls.py) - Roteamento
```

### Estrutura de Aplicação Django
- **core/** - Configurações globais do projeto
- **core_app/** - Aplicação principal com modelos e lógica
- **static/** - Arquivos estáticos (CSS, JS, imagens)
- **templates/** - Templates HTML

---

## 📦 Stack Completo

| Camada | Tecnologia | Versão |
|--------|-----------|--------|
| Backend | Django | 5.2.3 |
| Banco de Dados | MySQL | - |
| Frontend | HTML5, CSS3, JavaScript ES6+ | - |
| Testes | pytest | - |
| Async Support | asgiref | 3.11.1 |
| Configuração | django-environ, python-dotenv | 0.12.0, - |

---

## 🚀 Como Executar

1. **Instalar dependências:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configurar banco de dados:**
   ```bash
   python manage.py migrate
   ```

3. **Executar servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

4. **Rodar testes:**
   ```bash
   pytest
   ```

---

**Último atualizado:** Fevereiro 2026
