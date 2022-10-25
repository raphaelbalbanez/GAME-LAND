from django.shortcuts import render, redirect
from core.models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import Usuarioform
from .models import Comentario, Perfil
from datetime import datetime, timedelta

@login_required(login_url='/login/')
def criar_coment(request):
    id_coment = request.GET.get('id')
    dados = { }
    if id_coment:
        dados['coment'] = Comentario.objects.get(id=id_coment)
    return render(request, 'veranuncio.html', dados)

@login_required(login_url='/login/')
def editar_coment(request):
    if request.POST:
        comentario = request.POST.get('comentario')
        usuario = request.user
        id_post = request.POST.get('id_coment') 
        if id_post:
            Comentario.objects.filter(usuario=usuario).update(comentario=comentario)
        else:
            Comentario.objects.create(comentario=comentario, usuario=usuario)
    return redirect('/')

@login_required(login_url='/login/')
def lista_coments(request):
    coment = Comentario.objects.filter()
    dados = {'coments': coment}
    return render(request, 'veranuncio.html', dados)

@login_required(login_url='/login/')
def lista_posts_historico(request):
    usuario = request.user
    data_atual = datetime.now()
    post = Post.objects.filter(usuario=usuario, data_criacao__lt=data_atual)
    dados = {'posts':post}
    return render(request, 'historico.html', dados)

@login_required(login_url='/login/')
def infoanuncio(request):
    id_post = request.GET.get('id')
    post = Post.objects.filter(id=id_post)
    dados = {'posts': post}
    return render(request, 'veranuncio.html', dados)
    
def criar_usuario(request):
    form = Usuarioform(request.POST)
    if request.method =="POST":
        form = Usuarioform(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            return redirect('/')
    return render(request, 'cadastrar.html', {'form':form})  

@login_required(login_url='/login/')
def atualizar_dados(request):
    if request.POST:
        nome_completo = request.POST.get('nome_completo')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        usuario = request.user
        id_perfil = request.POST.get('id_perfil') 
        if id_perfil:
            Perfil.objects.filter(usuario=usuario).update(nome_completo=nome_completo, cpf=cpf, telefone=telefone)
        else:
            Perfil.objects.create(nome_completo=nome_completo, cpf=cpf, telefone=telefone, usuario=usuario)
    return redirect('/')

@login_required(login_url='/login/')
def dados_perfil(request):
    usuario = request.user
    perfil = Perfil.objects.filter(usuario=usuario)
    dados = {'perfils': perfil}
    return render(request, 'meusdados.html', dados)
    

@login_required(login_url='/login/')
def criar_perfil(request):
    id_perfil = request.GET.get('id')
    dados = { }
    if id_perfil:
        dados['perfil'] = Perfil.objects.get(id=id_perfil)
    return render(request, 'atualizardados.html', dados)

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
    # usuario = request.user
    post = Post.objects.filter()
    dados = {'posts': post}
    return render(request, 'home.html', dados)

@login_required(login_url='/login/')
def posts_usuario(request):
    usuario = request.user
    post = Post.objects.filter(usuario=usuario)
    dados = {'posts': post}
    return render(request, 'meusanuncios.html', dados)

@login_required(login_url='/login/')
def anunciar(request):
    id_post = request.GET.get('id')
    dados = { }
    if id_post:
        dados['post'] = Post.objects.get(id=id_post)
    return render(request, 'anunciar.html', dados)

@login_required(login_url='/login/')
def submit_anunciar(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        Preço = request.POST.get('Preço')
        usuario = request.user
        id_post = request.POST.get('id_post') 
        if id_post:
            Post.objects.filter(usuario=usuario).update(titulo=titulo, descricao=descricao, Preço=Preço)
        else:
            Post.objects.create(titulo=titulo, descricao=descricao, Preço=Preço, usuario=usuario)
    return redirect('/')

@login_required(login_url='/login/')
def delete_anuncio(request, id_post):
    usuario = request.user
    post = Post.objects.get(id=id_post)
    if usuario == post.usuario:
        post.delete()
    return redirect('/')

 
