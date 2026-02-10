# 🏥 FilaZero+ (Monitoramento de Lotação Hospitalar)

> "Menos filas, mais saúde. Decisões informadas antes de sair de casa."

## 📌 Sobre o Projeto
O **FilaZero+** é uma solução web desenvolvida para combater a superlotação em unidades de saúde. O sistema oferece transparência em tempo real para a população, permitindo que pacientes com casos menos urgentes verifiquem a lotação das unidades próximas e escolham onde ser atendidos, equilibrando a demanda da rede pública/privada.

### 🎯 A Dor (Problema)
Pacientes se deslocam para postos de saúde sem saber o tempo de espera real. Isso gera:
1.  Aglomerações desnecessárias.
2.  Risco de contágio cruzado em salas de espera lotadas.
3.  Desgaste das equipes médicas.

### 💡 A Solução
Um sistema de **"Semáforo de Lotação"**:
* **Visão do Cidadão:** Acesso web simples (sem login) que mostra as unidades, endereço e um indicador de cor (🟢 Livre, 🟡 Moderado, 🔴 Lotado).
* **Visão da Unidade:** Painel administrativo minimalista onde a recepção atualiza o fluxo com apenas dois cliques (+ Entrada / - Saída).

---

## 🚀 Tecnologias Utilizadas
* **Backend:** Python 3 + Django 5
* **Banco de Dados:** MySQL
* **Frontend:** HTML5, CSS3, JavaScript (Fetch API para atualização em tempo real)
* **Estilização:** Bootstrap / CSS Customizado

---

## 🛠️ Instalação e Execução

### Pré-requisitos
* Python 3.x
* MySQL Server rodando

### Passo a passo
1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU_USUARIO/filazero-plus.git](https://github.com/SEU_USUARIO/filazero-plus.git)
    cd filazero-plus
    ```

2.  **Crie o ambiente virtual e instale dependências:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    pip install -r requirements.txt
    ```

3.  **Configure o Banco de Dados:**
    * Crie um banco chamado `filazero_db` no seu MySQL.
    * Ajuste as credenciais no arquivo `settings.py`.

4.  **Rode as migrações e inicie:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```

---

## 📋 Status do Projeto
* [x] Definição de Escopo
* [ ] Backend (Models & Views)
* [ ] Frontend (Interface do Cidadão)
* [ ] Integração com Banco de Dados
* [ ] Testes e Validação
