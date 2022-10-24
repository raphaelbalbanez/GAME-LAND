from django.contrib import admin
from core.models import Post
from .models import Perfil
from .models import Comentarios

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'Preço')
    # readonly_fields = ('view_imagem',)
    # list_filter = ('usuario', 'Preço')

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'telefone')

class ComentariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'comentario', 'usuario')

admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comentarios, ComentariosAdmin)
