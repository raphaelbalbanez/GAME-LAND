from django.contrib import admin
from core.models import Post
from .models import Perfil

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'Preço')
    # list_filter = ('usuario', 'Preço')

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'telefone')

admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Post, PostAdmin)
