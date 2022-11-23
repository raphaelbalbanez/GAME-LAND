from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from core.models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import Usuarioform
from .forms import CommentForm
from .models import Comment, Perfil
from datetime import datetime, timedelta

@login_required(login_url='/login/')
def darlike(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('/GAMELAND/'+str(post.id))

@login_required(login_url='/login/')
def addcomment(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.name = form.cleaned_data['name']
            data.comment = form.cleaned_data['comment']
            data.post_id = id
            data.save()
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)



# @login_required(login_url='/login/')
# def lista_posts_historico(request):
#     usuario = request.user
#     data_atual = datetime.now()
#     post = Post.objects.filter(usuario=usuario, data_criacao__lt=data_atual)
#     dados = {'posts':post}
#     return render(request, 'historico.html', dados)

def post_detail(request, id):
    post = Post.objects.get(pk=id) 
    comments = Comment.objects.filter(post_id=id)
    tem_like = request.user in post.likes.all()
    total = 0
    for i in comments:
        total = total + 1
    
    context = {
        'post': post,
        'comments': comments,
        'total': total,
        'posts': post,
        'likes': post.quantidade_likes(),
        'tem_like': tem_like
        }

    return render(request, 'veranuncio.html', context)

# @login_required(login_url='/login/')
# def infoanuncio(request):
#     id_post = request.GET.get('id')
#     post = Post.objects.filter(id=id_post)
#     dados = {'posts': post}
#     return render(request, 'veranuncio.html', dados)
    
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


class AuthorCreateView(SuccessMessageMixin,):
    model = User
    success_url = '/success/'
    success_message = "%(name)s was created successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.calculated_field,
        )