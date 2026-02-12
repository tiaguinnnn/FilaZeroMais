from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UnidadeSaude

def home(request):
    return render(request, 'core_app/home.html')

@login_required
def servicos(request):
    unidades = UnidadeSaude.objects.all()
    return render(request, 'core_app/servicos.html', {'unidades': unidades})

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

        user = User.objects.create_user(
            username=username,
            password=password1,
            first_name=first_name
        )

        # login automático
        login(request, user)

        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('servicos')

    return render(request, 'core_app/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return redirect('login')

    return render(request, 'core_app/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')