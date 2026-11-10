class Categoria:

    #definindo atributos
    def __init__(self, nome):
        self.__nome = nome

    #definido propriedade e método para atributo nome
    @property
    def nome(self):
        return self.__nome
        
    #definindo método para renomear
    def renomear(self, nome):
        nome = nome.strip()
        #icluindo regra de negócio
        if nome == "":
            raise ValueError("Nome não pode ser vazio")

    def __str__(self):
        return f"{self.__nome}"
        
