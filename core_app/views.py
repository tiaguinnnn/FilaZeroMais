from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Páginas públicas
def home(request):
    return render(request, 'core_app/home.html')

def sobre(request):
    return render(request, 'core_app/sobre.html')

def servicos(request):
    return render(request, 'core_app/servicos.html')

def contato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        # Aqui você pode salvar no banco ou enviar email
        messages.success(request, 'Mensagem enviada com sucesso!')
        return redirect('contato')
    return render(request, 'core_app/contato.html')

# Cadastro
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')

        if password1 != password2:
            messages.error(request, 'As senhas não coincidem.')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já existe.')
            return redirect('register')

        user = User.objects.create_user(username=username, password=password1, first_name=first_name)
        user.save()
        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('login')

    return render(request, 'core_app/register.html')

# Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # email
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return redirect('login')
    return render(request, 'core_app/login.html')

# Logout
def logout_view(request):
    logout(request)
    return redirect('home')

# Dashboard (somente usuários logados)
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'core_app/dashboard.html')
