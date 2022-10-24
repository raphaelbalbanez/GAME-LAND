from enum import unique
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
    
    class Meta:
        db_table = 'post'
    
    def __str__(self):
        return self.titulo
    
    def get_data_post(self):
        return self.data_criacao.strftime('%d/%m/%Y %H:%M Hrs')

class Perfil(models.Model):
    nome_completo = models.CharField(max_length=70, null=True)
    cpf = models.CharField(max_length=14, null=True)
    telefone = models.CharField(max_length=16, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)


class Comentario(models.Model):
    comentario = models.TextField(blank=False, null=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


