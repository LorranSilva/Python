class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

        @property
        def nome(self):
            return self._nome

        """@nome.setter
        def nome(self, name):
            self._nome = name.upper()
        """
        @property
        def idade(self):
            return self._idade

        """@idade.setter
        def idade(self, age):
            self._idade = age"""


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)  # Inicializa nome e idade
        self.conta = None

    def inserir_conta(self, conta):
        self.conta = conta
