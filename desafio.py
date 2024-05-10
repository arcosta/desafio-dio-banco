from desafio_oo import PessoaFisica,Conta
from datetime import datetime as dt

menu_principal = '''

[d] Depositar
[s] Sacar
[e] Extrato
[u] Novo usuário
[lu] Listar usuários
[c] Nova conta
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
    global usuarios

    print("Cadastro de usuário")
    nome = input("Nome do novo usuario: ")
    endereco = input("Endereço: ")
    data_nascimento = input("Data de nascimento: ")
    cpf_cru = input("CPF: ")

    cpf = transforma_cpf(cpf_cru)

    # Validacoes
    for u in usuarios:
        if u['cpf'] == cpf:
            print(f"Usuario já cadastrado com o {cpf=}")
            return

    usuarios.append(
        {
            'nome': nome,
            'endereco': endereco,
            'data_nascimento': data_nascimento,
            'cpf': cpf
        }
    )

def transforma_cpf(cpf_cru):
    tabela_transposicao = str.maketrans({'.': '', '-':''})
    return cpf_cru.translate(tabela_transposicao)


def cadastra_conta():
    print("Cadastro de contas")
    cpf_cru = input("Digite o cpf do dono da conta")
    cpf = transforma_cpf(cpf_cru)

    for u in usuarios:
        if u['cpf'] == cpf:
            contas.append(
                {
                    'numero': len(contas)+1,
                    'agencia': "0001",
                    'cpf': cpf
                }
            )
    print("Não existe usuário cadastrado para o CPF informado")

def nova_conta():
    ...
def listar_usuarios():
    for user in usuarios:
        print(user)


def novo_usuario():
    print('''
    === NOVO USUARIO ===''')
    nome = input('Nome: ')
    cpf = transforma_cpf( input('CPF: ') )
    str_dn = input('Data de nascimento (dd/mm/yyyy): ')
    data_nascimento = dt.strptime (
        str_dn.strip() + ' 00:00:00',
        '%d/%m/%Y %H:%M:%S'
    )
    endereco = input('Endereço: ')

    pf = PessoaFisica(cpf, nome, data_nascimento, endereco)

    usuarios.append(pf)

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
usuarios = list()
contas = list()


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
    elif opcao == 'c':
        nova_conta()
    elif opcao == 'u':
        novo_usuario()
    elif opcao == 'lu':
        listar_usuarios()
    else:
        print('Opção inválida. Por favor, selecione novamente a operação desejada')

