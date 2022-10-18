from django.db import models
from django.contrib.auth.models import User
from distutils.command.upload import upload
from django.utils.html import mark_safe

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now=True)
    Preço = models.FloatField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    # imagem = models.ImageField(upload_to="post",blank=True, null=True)


    class Meta:
        db_table = 'post'
    
    def __str__(self):
        return self.titulo

class Perfil(models.Model):
    nome_completo = models.CharField(max_length=70, null=True)
    cpf = models.CharField(max_length=14, null=True)
    telefone = models.CharField(max_length=16, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

# @property
# def view_image(self):
#     return mark_safe('img scr = "%s" whidth="400px" /> '%self.imagem.url)
#     view_image.short_description = "imagem cadastrada"
#     view_image.allow_tags = True



