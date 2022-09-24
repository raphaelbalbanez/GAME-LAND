from django.shortcuts import render, redirect
from core.models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválido")
    return redirect('/')

@login_required(login_url='/login/')
def lista_posts(request):
    usuario = request.user
    post = Post.objects.filter(usuario=usuario)
    dados = {'posts': post}
    return render(request, 'home.html', dados)