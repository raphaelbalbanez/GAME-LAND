from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now=True)
