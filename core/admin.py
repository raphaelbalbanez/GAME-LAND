from django.contrib import admin
from core.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'Preço')
    list_filter = ('usuario', 'Preço')


admin.site.register(Post, PostAdmin)