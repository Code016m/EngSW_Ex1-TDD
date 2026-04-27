# test_filtro_livros.py

from lista_livros import obter_livros
from filtro_livros import filtrar_livros
import unittest

class TestFiltroLivros(unittest.TestCase):
    def setUp(self):
        self.livros = obter_livros()
    def test_filtrar_por_autor(self):
        resultado = filtrar_livros(self.livros, {'autor': 'Autor 1'})
        self.assertEqual(len(resultado), 2)
        print(resultado)
    def test_filtrar_categoria(self):
        resultado = filtrar_livros(self.livros, {'categoria': 'Ficção'})
        self.assertEqual(len(resultado), 2)
    def test_filtrar_preco_max(self):
        resultado = filtrar_livros(self.livros, {'preco_max': 40})
        self.assertEqual(len(resultado), 2)
        print(resultado)
    def test_filtrar_preco_min(self):
        resultado = filtrar_livros(self.livros, {'preco_min': 50})
        self.assertEqual(len(resultado), 2)
        print(resultado)
    def test_filtrar_combinado(self):
        resultado = filtrar_livros(self.livros, {
            'autor': 'Autor 1',
            'preco': 35
        })
        self.assertEqual(len(resultado), 2)
        print(resultado)
