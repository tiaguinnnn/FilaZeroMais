from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from validate_docbr import CPF

# Importamos os dois modelos: o seu e o da sua colega
from .models import UnidadeSaude, Paciente

# =========================
# PÁGINAS PÚBLICAS
# =========================

def home(request):
    return render(request, 'core_app/home.html')

def sobre(request):
    return render(request, 'core_app/sobre.html')

def unidade(request):
    return render(request, 'core_app/unidade.html')

def servicos(request):
    """
    Lista todas as unidades de saúde para os visitantes.
    """
    unidades = UnidadeSaude.objects.all().order_by('pacientes_em_espera')
    return render(request, 'core_app/servicos.html', {'unidades': unidades})

def contato(request):
    if request.method == 'POST':
        messages.success(request, 'Mensagem enviada com sucesso!')
        return redirect('contato')
    return render(request, 'core_app/contato.html')

# =========================
# AUTENTICAÇÃO
# =========================

def register_view(request):
    if request.method == 'POST':
        # Coleta de dados
        username = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        cpf_input = request.POST.get('cpf')
        telefone = request.POST.get('telefone')

        # --- CAMADA DE VALIDAÇÃO PRO ---

        # 1. Validação de Tamanho Mínimo
        if len(password1) < 6:
            messages.error(request, 'A senha deve ter no mínimo 6 caracteres.')
            return render(request, 'core_app/register.html')
        
        if len(first_name) < 3:
            messages.error(request, 'O nome deve ter no mínimo 3 caracteres.')
            return render(request, 'core_app/register.html')
        
        if len(telefone) <= 10:
            messages.error(request, 'Telefone deve conter no minimo 11 números.')
            return render(request, 'core_app/register.html')

        # 2. Comparação de Senhas
        if password1 != password2:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'core_app/register.html')

        # 3. Validação de CPF (API Local)
        cpf_validator = CPF()
        if not cpf_validator.validate(cpf_input):
            messages.error(request, 'CPF Inválido! Verifique os dígitos.')
            return render(request, 'core_app/register.html')

        # 2. Formata o CPF (Ex: 12345678900 -> 123.456.789-00) para padronizar no banco
        cpf_formatted = cpf_validator.mask(cpf_input)

        # 3. Verifica se JÁ EXISTE no banco de dados (Unicidade)
        if Paciente.objects.filter(cpf=cpf_formatted).exists():
            messages.error(request, 'Este CPF já possui cadastro no sistema.')
            return render(request, 'core_app/register.html')
        
        # Se passar por tudo, salva!
        try:
            user = User.objects.create_user(
                username=username, 
                password=password1, 
                first_name=first_name, 
                email=username
            )
            
            Paciente.objects.create(
                user=user,
                nome=first_name,
                cpf=cpf_formatted, # Salva formatado
                telefone=telefone,
                email=username
            )
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login')
        
        except Exception as e:
            messages.error(request, 'Erro interno ao cadastrar. Tente novamente.')
            return render(request, 'core_app/register.html')

    return render(request, 'core_app/register.html')

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )

        if user:
            auth_login(request, user)
            return redirect('dashboard')

        messages.error(request, 'Usuário ou senha inválidos.')
        return redirect('login')

    return render(request, 'core_app/login.html')

def logout_view(request):
    auth_logout(request)
    return redirect('home')

# =========================
# ÁREA LOGADA
# =========================

@login_required(login_url='login')
def dashboard(request):
    """
    Mostra as unidades para o funcionário logado poder acompanhar.
    """
    unidades = UnidadeSaude.objects.all()
    return render(request, 'core_app/dashboard.html', {'unidades': unidades})