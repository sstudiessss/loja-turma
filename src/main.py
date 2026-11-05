from models.categoria import Categoria
from models.produto import Produto
from models.cliente import Cliente

eletronicos = Categoria("Eletrônicos")
notebook = Produto("Notebook", 3500, 5, eletronicos)
mouse = Produto("Mouse", 100, 20, eletronicos)

maria = Cliente("Maria", "maria@email.com")
print("Carrinho novo:", maria.carrinho)

maria.carrinho.adicionar(notebook, 1)
maria.carrinho.adicionar(mouse, 1)
maria.carrinho.adicionar(mouse, 1)        # repetido: aumenta a quantidade
print(maria.carrinho)
print("Quantos itens na lista:", len(maria.carrinho.itens))

try:
    maria.carrinho.adicionar(notebook, 10)
except ValueError as erro:
    print("Erro:", erro)

maria.carrinho.remover(mouse)
print("Depois de remover o mouse:")
print(maria.carrinho)