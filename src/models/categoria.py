"""Classe Categoria (Aula 3)."""


class Categoria:
    """Agrupa produtos parecidos. Ex.: "Eletrônicos", "Livros"."""

    def __init__(self, nome):
        # Construtor: é chamado automaticamente quando fazemos Categoria("Livros")
        self.__nome = ""          # atributo PRIVADO (dois sublinhados)
        self.renomear(nome)       # reaproveita a validação do método

    @property
    def nome(self):
        """Permite LER o nome (categoria.nome), mas não alterar diretamente."""
        return self.__nome

    def renomear(self, nome):
        """Única forma de alterar o nome: com validação (encapsulamento)."""
        nome = nome.strip()
        if nome == "":
            raise ValueError("O nome da categoria não pode ser vazio.")
        self.__nome = nome

    def __str__(self):
        # __str__ define o que aparece quando fazemos print(categoria)
        return self.__nome
