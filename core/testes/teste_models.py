from typing_extensions import Self
import unittest
from django.test import TestCase

class TestUsuario(unittest.TestCase):

  def TestPost(Self):
    def setUP (self):
        self.admin1 = Admin('Rapha')
        

    def test_titulo(self):
      self.assertEqual(self.admin.titulo, 'gtaV')

    def test_usuario(self):
      self.assertEqual(self.admin.usuario, 'Rapha')
      
    def test_preco(self):
      self.assertEqual(self.admin.preco, '20.00')

    def test_descricao(self):
      self.assertEqual(self.admin.descricao, 'jogo novo')

    def test_data(self):
      self.assertEqual(self.admin.descricao, '12/10')


    
    def test_nome(self):
      self.assertEqual(self.admin2.nome, 'hugo')

    def test_cpf(self):
      self.assertEqual(self.admin2.cpf, '085*******')

    def test_cel(self):
      self.assertEqual(self.admin2.cel, '81 998471385')
    
    def test_usuario1(self):
      self.assertEqual(self.admin2.usuario, 'Rapha')

if __name__ == '__main__':
  unittest.main()
        
