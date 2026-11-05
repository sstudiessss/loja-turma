class Cliente:
    """Pessoa que compra na loja."""

    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = ""
        self.atualizar_email(email)        # RN3: e-mail precisa ter @

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    def atualizar_email(self, valor):
        """Encapsulamento: só aceita e-mail com @."""
        if "@" not in valor:
            raise ValueError(f"E-mail inválido: {valor}")
        self.__email = valor.strip().lower()

    def __str__(self):
        return f"{self.__nome} <{self.__email}>"