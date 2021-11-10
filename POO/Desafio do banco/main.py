from conta import ContaCorrente, ContaPoupanca
from banco import Banco
from pessoa import Cliente

banco = Banco()

cliente1 = Cliente('João', 43)
cliente2 = Cliente('Larissa', 23)
cliente3 = Cliente('Lucrecia', 61)
cliente4 = Cliente('Gustavo', 43)


conta1 = ContaPoupanca(111, 234, 123.98)
conta2 = ContaPoupanca(222, 543, 100.00)
conta3 = ContaCorrente(333, 433, 00.00)
conta4 = ContaCorrente(444, 343, 35.00)
