from abc import ABC, abstractclassmethod


class Conta(ABC):
    def __init__(self, agencia, num, saldo):
        self.agencia = agencia
        self.num = num
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    @abstractclassmethod
    def sacar(self, valor):
        pass


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo para saque insuficiente!')
            return

        self.saldo -= valor


class ContaCorrente(Conta):
    def __init__(self, agencia, num, saldo, limite=150):
        super().__init__(agencia, num, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor > (self.saldo + self.limite):
            print('Saldo para saque insuficiente!')
            return

        self.saldo -= valor
