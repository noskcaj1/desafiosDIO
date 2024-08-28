#Detalhes do código: Ler o README

# Constantes
LIMITE_SAQUES = 3
LIMITE_SAQUE_VALOR = 500

# Variáveis globais
saldo = 0
extrato = ""
numero_saques = 0

# Funções
def exibir_menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    return input(menu)

def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

def sacar(valor):
    global saldo, numero_saques, extrato
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > LIMITE_SAQUE_VALOR
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print(f"Operação falhou! O valor do saque excede o limite de R$ {LIMITE_SAQUE_VALOR:.2f}.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

def exibir_extrato():
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Loop principal
while True:
    opcao = exibir_menu()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        depositar(valor)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        sacar(valor)

    elif opcao == "e":
        exibir_extrato()

    elif opcao == "q":
        print("Obrigado por utilizar nosso sistema bancário. Até logo!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
