🏥 FilaZero+ (Monitoramento de Lotação Hospitalar)
"Menos filas, mais saúde. Transparência e eficiência para a gestão hospitalar."

📌 Sobre o Projeto
O FilaZero+ é uma plataforma focada em resolver o problema de superlotação em unidades de saúde. Através de um sistema de "Semáforo de Lotação", pacientes podem verificar a ocupação de hospitais e UBSs em tempo real antes de sair de casa, permitindo uma distribuição inteligente da demanda.

🛠️ Tecnologias Utilizadas
Back-end: Python 3.12+ & Django 5.0

Banco de Dados: MySQL 8.0

Testes: Pytest & Pytest-Django

Infra: Script de Provisionamento Automático (init_db)

🚀 Guia de Instalação e Execução
Siga rigorosamente os passos abaixo para preparar o ambiente:

1. Clonar e Configurar Ambiente
Bash
# Clone o projeto
git clone https://github.com/tiaguinnnn/FilaZeroMais.git
cd FilaZeroMais

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate # Linux/Mac

# INSTALAÇÃO DE DEPENDÊNCIAS (Não pule este passo)
pip install django mysql-connector-python python-dotenv pytest pytest-django
2. Configurar Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto com suas credenciais do MySQL local:

Snippet de código
DB_NAME=filazero_db
DB_USER=root
DB_PASSWORD=VoucherDev@2024
DB_HOST=localhost
3. Provisionamento do Banco de Dados
Executamos o setup em 3 etapas para garantir que o banco exista e esteja populado:

Bash
# A) Criação física do banco no MySQL
python init_db.py

# B) Aplicação da estrutura das tabelas
python manage.py makemigrations
python manage.py migrate

# C) Fomento de dados realistas (UBSs e Hospitais)
python manage.py seed_db
4. Rodar o Projeto
Bash
python manage.py runserver
O sistema estará disponível em: http://127.0.0.1:8000

🧪 Validação de Qualidade (QA)
Para rodar os testes automatizados de integridade de dados e segurança:

Bash
pytest -v
📋 Funcionalidades Principais
[x] Dashboard de Unidades: Visualização de lotação via cores dinâmicas.

[x] Cadastro de Paciente: Validação robusta de CPF e vínculo com Django User.

[x] Monitoramento em Tempo Real: Contador de pacientes em espera com travas de segurança (MinValueValidator).

[x] Provisionamento DevOps: Script para recriação rápida de ambiente.

🤝 Contribuição
Desenvolvido por Tiago, Erica e Eric para o Hackathon 2026.
