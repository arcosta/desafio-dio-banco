menu_principal = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>'''

def saque(*,saldo, valor, limite, numero_saques, limite_saques):
    print('Saque')
        
    
    if saldo <= 0 or valor > saldo:
        print('Saldo insuficiente')
    if valor > limite:
        print('Limite excedido')
    if numero_saques > limite_saques:
        print('Limite de saques diário excedido')
    numero_saques += 1
    historico.append(f'R$ {valor:.2f}D')
    saldo -= valor

    return saldo,historico


def deposito():
    global saldo
    global extrato
    global menu_deposito

    print('Depósito')
    valor = float(input(menu_deposito))
    historico.append(f"R$ {valor:.2f}C")
    saldo += valor

def extrato():
    global historico
    global saldo

    print('Extrato')
    for movimentacao in historico:
        print(movimentacao)
    print(f"Saldo atual: R$ {saldo:.2f}")

def cadastra_usuario():
    ...

def cadastra_conta():
    ...

menu_saque = '''
=== SAQUE ===
Entre com o valor a ser sacado
=>'''

menu_deposito = '''
=== DEPÓSITO ===
Entre com o valor a ser depositado
=>'''

saldo = 0
limite = 500
historico = list()
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu_principal)
    if opcao == 'd':
        deposito()

    elif opcao == 's':
        valor = input(menu_saque)
        saldo, extrato = saque(saldo=saldo, valor=valor, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
        
    elif opcao == 'e':
        extrato()

    elif opcao == 'q':
        break
    else:
        print('Opção inválida. Por favor, selecione novamente a operação desejada')

