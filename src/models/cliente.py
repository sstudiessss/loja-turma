class Cliente:
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = None
        self.atualizar_email(email)
        self.__pedidos = []

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @property
    def pedidos(self):
        return self.__pedidos

    def atualizar_email(self, email):
        email = email.strip()
        if email == "":
            raise ValueError("Email não pode ser vazio")
        if "@" not in email: #RN3 email deve conter caractere @ para ser valido
            raise ValueError("Email inválido, deve conter caractere @")
        self.__email = email

    def __str__(self):
        return f"Nome: {self.__nome}, Email: {self.__email}, Pedidos: {len(self.__pedidos)}"
