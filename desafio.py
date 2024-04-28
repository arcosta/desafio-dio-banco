menu_principal = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>'''

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
extrato = list()
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu_principal)
    if opcao == 'd':
        print('Depósito')
        valor = float(input(menu_deposito))
        extrato.append(f"R$ {valor:.2f}C")
        saldo += valor

    elif opcao == 's':
        print('Saque')
        
        valor = input(menu_saque)
        if saldo <= 0 or valor > saldo:
            print('Saldo insuficiente')
        if valor > limite:
            print('Limite excedido')
        if numero_saques > LIMITE_SAQUES:
            print('Limite de saques diário excedido')
        numero_saques += 1
        extrato.append(f'R$ {valor:.2f}D')
        saldo -= valor
        
    elif opcao == 'e':
        print('Extrato')
        for movimentacao in extrato:
            print(movimentacao)
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == 'q':
        break
    else:
        print('Opção inválida. Por favor, selecione novamente a operação desejada')

