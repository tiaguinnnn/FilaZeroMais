# 🏥 FilaZero+ - Monitoramento de Lotação Hospitalar

**Plataforma para visualizar lotação de hospitais e UBSs em tempo real via "Semáforo de Lotação"**

---

## 🚀 Instalação Rápida (em 6 passos)

### 1️⃣ Clonar Repositório

```powershell
git clone https://github.com/tiaguinnnn/FilaZeroMais.git
cd FilaZeroMais
```

### 2️⃣ Criar e Ativar Ambiente Virtual

```powershell
python -m venv venv
venv\Scripts\activate
```

**Para Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instalar Dependências

```powershell
pip install -r requirements.txt
```

### 4️⃣ Configurar Banco de Dados

Crie um arquivo `.env` na raiz com:

Depois provisione:

```powershell
python init_db.py
python manage.py makemigrations
python manage.py migrate
python manage.py seed_db
```

### 5️⃣ Criar Usuário Admin (opcional)

```powershell
python manage.py createsuperuser
```

### 6️⃣ Rodar Servidor

```powershell
python manage.py runserver
```

Acesse: **http://127.0.0.1:8000/**

---

## 📋 Rodar Testes Completos

```powershell
# Todos os testes
pytest -v

# Teste específico
pytest core_app/test/test_db.py -v
pytest core_app/test/test_cpf_db.py -v
pytest core_app/test/test_rotas.py -v
```

---

## 🔧 Comandos Principais

```powershell
# Ativar ambiente virtual
venv\Scripts\activate

# Desativar ambiente virtual
deactivate

# Instalar dependências
pip install -r requirements.txt

# Criar tabelas no BD
python manage.py migrate

# Rodar servidor
python manage.py runserver

# Criar admin
python manage.py createsuperuser

# Testes
pytest -v
```

---

## 🐛 Troubleshooting

### Erro: MySQL não conecta

```powershell
# 1. Verificar se MySQL está rodando
mysql --version

# 2. Verificar credenciais em .env
type .env

# 3. Recriar banco
python init_db.py
```

### Erro: Tabelas não encontradas

```powershell
python manage.py makemigrations
python manage.py migrate
```

### Erro: ModuleNotFoundError

```powershell
# Reativar ambiente virtual
venv\Scripts\activate

# Reinstalar dependências
pip install -r requirements.txt --force-reinstall
```

### Ambiente Virtual não ativa (PowerShell)

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\activate
```

---

## 📦 Dependências

- **Python 3.12+**
- **MySQL 8.0+**
- **Django 5.2.3**
- **Pytest** (testes)

Ver `requirements.txt` para lista completa.

---

## 🎯 Estrutura Básica

```
FilaZeroMais/
├── manage.py              # Comandos Django
├── init_db.py             # Setup BD
├── requirements.txt       # Dependências
├── .env                   # Variáveis (criar)
├── core/                  # Configurações
├── core_app/              # App principal
│   ├── models.py          # Modelos
│   ├── views.py           # Lógica
│   └── test/              # Testes
└── templates/             # HTML
```

---

## ✅ Checklist de Funcionamento

- [ ] Python 3.12+ instalado
- [ ] MySQL 8.0+ instalado e rodando
- [ ] `pip install -r requirements.txt` ✅
- [ ] `.env` configurado
- [ ] `python init_db.py` ✅
- [ ] `python manage.py migrate` ✅
- [ ] `python manage.py seed_db` ✅
- [ ] `python manage.py runserver` ✅ (sem erros)
- [ ] `pytest -v` ✅ (todos passando)

---

---

**Desenvolvido para Hackathon 2026 - Senac**
