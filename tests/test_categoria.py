import unittest

from models.categoria import Categoria


class TestCategoria(unittest.TestCase):

    def test_criar_categoria(self):
        livros = Categoria("Livros")
        self.assertEqual(livros.nome, "Livros")

    def test_renomear_categoria(self):
        categoria = Categoria("Livro")
        categoria.renomear("Livros")
        self.assertEqual(categoria.nome, "Livros")

    def test_nome_vazio_gera_erro(self):
        with self.assertRaises(ValueError):
            Categoria("   ")

    def test_print_mostra_o_nome(self):
        self.assertEqual(str(Categoria("Livros")), "Livros")
