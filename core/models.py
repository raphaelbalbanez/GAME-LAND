##from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from distutils.command.upload import upload
from django.utils.html import mark_safe
from datetime import datetime, timedelta

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now=True)
    Preço = models.FloatField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='post_likes')
    imagem = models.ImageField(upload_to='imagens/', default='imagem')
    
    class Meta:
        db_table = 'post'
    
    def __str__(self):
        return self.titulo         
    
    def get_data_post(self):
        return self.data_criacao.strftime('%d/%m/%Y %H:%M Hrs')
    
    def quantidade_likes(self):
        return self.likes.count()

class Perfil(models.Model):
    nome_completo = models.CharField(max_length=70, null=True)
    cpf = models.CharField(max_length=14, null=True)
    telefone = models.CharField(max_length=16, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_completo
    

class Comment(models.Model):
    STATUS = (
        ('Lido', 'Lido'),
        ('Nao lido', 'Nao lido'),
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    name = models.CharField(max_length=255, null=False, blank=False)
    comment = models.TextField(null=True)

    status = models.CharField(choices=STATUS, max_length=10, default="Nao lido")

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name




