class Conta:
    def __init__(self):
        self.historico = list()
        self.saldo = 0.0
        self.limite_por_saque = 500.0
        self.


    def deposito(self, valor):
        if valor <= 0:
            raise ValueError
        self.historico.append(f"+ {valor}")
        self.saldo += valor

        
    def extrato(self):
        return self.historico
        
    def saque(self, valor):
        if valor <= 0:
            raise ValueError
        if valor > self.limite_por_saque:
            raise ValueError
        self.historico.append(f"- {valor}")
        self.saldo -= valor

class Usuario:
    ...

