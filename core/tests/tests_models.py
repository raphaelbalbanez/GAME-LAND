from typing_extensions import Self
import unittest
from django.test import TestCase
from ..models import Post
from ..models import User
from ..models import Perfil
from ..models import Comment

class PostTestCase(unittest.TestCase):
  
  
        
  
  def setUp (self):
        
        user=User.objects.filter(username = 'raphael').first()

        ##Perfil.objects.create(
          ##nome_completo="Raphael Barros",
          ##usuario=user,
          #telefone = '998471385'
          #)
        
        Post.objects.create(
          titulo='pes12',
          usuario=user,
          descricao='usado poucas vezes', 
          data_criacao='11/06/2003',
          Preço='10',
        )
  def test_retorno_str(self):
    teste_post = Post.objects.filter(titulo__contains='pes').first()
    self.assertEquals(teste_post.__str__(),'pes12')

    ##teste_post = Post.objects.get(data_criacao='2003/06/11')
    self.assertEquals(teste_post.descricao,'usado poucas vezes')

    self.assertEquals(teste_post.Preço,10.0)
    
    teste_Perfil = Perfil.objects.filter(nome_completo__contains='Raphael').first()
    self.assertEquals(teste_Perfil.__str__(),'Raphael Barros')
    self.assertEquals(teste_Perfil.telefone ,'998471385')
    self.assertEquals(teste_Perfil.cpf , None)

    teste_comentario = Comment.objects.filter(comment__icontains='r6').first()
    self.assertEquals(teste_comentario.__str__(),'hugocamp')

   

      
 
