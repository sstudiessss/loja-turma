from models.categoria import Categoria
from models.produto import Produto

eletronicos = Categoria ("Eletronicos")
pesca = Categoria ("Pesca")
casa = Categoria ("")

mouse = Produto("mouse", 2, 2, "Eletronicos")

#mouse.tem_estoque(1)
#print(mouse)

mouse.baixar_estoque(1)
print(mouse)