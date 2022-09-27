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
    
    def get_data_criacao(self):
        return self.data_criacao.strftime('%d/%m/%y %h %m ')