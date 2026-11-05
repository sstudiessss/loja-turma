import unittest

from models.categoria import Categoria
from models.produto import Produto


class TestProduto(unittest.TestCase):

    def setUp(self):
        # setUp roda ANTES de cada teste: cria objetos novos para cada um
        self.eletronicos = Categoria("Eletrônicos")
        self.notebook = Produto("Notebook", 3500, 5, self.eletronicos)

    def test_criar_produto(self):
        self.assertEqual(self.notebook.nome, "Notebook")
        self.assertEqual(self.notebook.preco, 3500.0)
        self.assertEqual(self.notebook.estoque, 5)

    def test_produto_conhece_a_categoria(self):
        self.assertIs(self.notebook.categoria, self.eletronicos)
        self.assertEqual(self.notebook.categoria.nome, "Eletrônicos")

    def test_preco_precisa_ser_maior_que_zero(self):
        with self.assertRaises(ValueError):
            Produto("Brinde", 0, 10, self.eletronicos)

    def test_estoque_nao_pode_ser_negativo(self):
        with self.assertRaises(ValueError):
            Produto("Brinde", 10, -1, self.eletronicos)

    def test_alterar_preco(self):
        self.notebook.alterar_preco(3300)
        self.assertEqual(self.notebook.preco, 3300.0)

    def test_atributo_privado_nao_e_acessivel(self):
        with self.assertRaises(AttributeError):
            self.notebook.__preco

    def test_baixar_estoque(self):
        self.notebook.baixar_estoque(2)
        self.assertEqual(self.notebook.estoque, 3)

    def test_nao_baixa_mais_que_o_estoque(self):
        with self.assertRaises(ValueError):
            self.notebook.baixar_estoque(10)

    def test_repor_estoque(self):
        self.notebook.repor_estoque(5)
        self.assertEqual(self.notebook.estoque, 10)
