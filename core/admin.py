from django.contrib import admin
from core.models import Post
from .models import Perfil
from .models import Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'Preço')
    # readonly_fields = ('view_imagem',)
    list_filter = ('usuario', 'Preço')

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'telefone')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
