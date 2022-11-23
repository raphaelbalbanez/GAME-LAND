from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment
from .models import Post

class Usuarioform(UserCreationForm):
    
    email = forms.EmailField(max_length=70)

    class Meta:
        model = User
        fields=['username', 'email', 'password1', 'password2']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment']

# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['imagem']
