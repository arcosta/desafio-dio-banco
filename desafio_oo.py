from __future__ import annotations
from abc import ABC
from datetime import date


class Transacao(ABC):
    def __init__(self, valor: float = 0.0):
        self.valor = valor
    
    def registrar(self, conta:Conta):
        ...

class Deposito(Transacao):
    def __init__(self, valor: float = 0.0):
        super().__init__(valor)

class Saque(Transacao):
    def __init__(self, valor: float = 0.0):
        super().__init__(valor)

class Historico:
    def __init__(self):
        self.transacao: list[Transacao] = []

    def adicionar_transacao(self, transacao: Transacao):
        self.transacao.append(transacao)


    
class Conta:
    def __init__(self, numero: int, cliente:Cliente, agencia: str = '001', saldo: float=0):
        super().__init__()
        self.numero = numero
        self.historico = Historico()
        self.cliente = cliente
        self.agencia = agencia
        self.saldo = saldo

    def saldo(self):
        ...
    def sacar(self):
        ...
    def depositar(self):
        ...

    @classmethod
    def nova_conta(cls, cliente:Cliente, numero:int):
        ...


class ContaCorrente(Conta):
    def __init__(self):
        self.limite = 0.0
        self.limite_saques = 0

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta:Conta, transacso: Transacao):
        ...

    def adicionar_conta(self, conta: Conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf: str, nome: str, data_nascimento: date, endereco: str):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento



#==============================================
