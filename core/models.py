from django.db import models
from django.contrib.auth.models import User

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

class Perfil(models.Model):
    nome_completo = models.CharField(max_length=70, null=True)
    cpf = models.CharField(max_length=14, null=True)
    telefone = models.CharField(max_length=16, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

