"""game_land URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('GAMELAND/', views.lista_posts),
    path('', RedirectView.as_view(url='/GAMELAND/')),
    path('GAMELAND/meus-anuncios/anunciar/', views.anunciar),
    path('GAMELAND/anunciar/', views.anunciar),
    path('GAMELAND/anunciar/submit', views.submit_anunciar),
    path('GAMELAND/meus-anuncios/anunciar/submit', views.submit_anunciar),
    path('GAMELAND/meus-anuncios/anunciar/delete/<int:id_post>/', views.delete_anuncio),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('cadastrar/', views.criar_usuario),
    path('GAMELAND/meus-dados/', views.dados_perfil),
    path('GAMELAND/meus-dados/atualizar-dados/', views.criar_perfil),
    path('GAMELAND/meus-dados/atualizar-dados/submit', views.atualizar_dados),
    path('GAMELAND/meus-anuncios/', views.posts_usuario),
    path('GAMELAND/<int:id>/', views.post_detail, name='post_detail' ),
    path('/GAMELAND/<int:id>/', views.favourite_post, name='favourite_post'),
    path('GAMELAND/favourites/', views.post_favourite_list, name='post_favourite_list'),
    # path('GAMELAND/meus-anuncios/historico/', views.lista_posts_historico),erro
    path('GAMELAND/ver-anuncio/<int:id>', views.addcomment, name="ver-anuncio"),
    path('like/<int:pk>/', views.darlike, name='dar_like'),
        
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
