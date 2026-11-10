from models.categoria import Categoria
from models.produto import Produto
from models.cliente import Cliente

eletronicos = Categoria ("Eletronicos")
pesca = Categoria ("Pesca")
casa = Categoria ("")

mouse = Produto("mouse", 2, 2, "Eletronicos")

#mouse.tem_estoque(1)
#print(mouse)

#mouse.baixar_estoque(1)
#print(mouse)

cliente_ID1 = Cliente("Ana", "ana@email.com")
cliente_ID2 = Cliente("João", "joao@email.com")
print(cliente_ID1, cliente_ID2)

cliente_ID1.atualizar_email("anamail.com")
print(cliente_ID1)
