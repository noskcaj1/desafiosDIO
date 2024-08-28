# 1-desafioDIO

Manual do Programa de Banco em Python
Introdução
Este manual tem como objetivo explicar de forma simples e didática cada parte do programa de banco em Python.

## Passo a Passo

### Constantes
LIMITE_SAQUES = 3
LIMITE_SAQUE_VALOR = 500
Constantes: Essas são variáveis cujo valor não muda durante a execução do programa.
LIMITE_SAQUES: Define o número máximo de saques permitidos por dia (3 saques).
LIMITE_SAQUE_VALOR: Define o valor máximo que pode ser sacado de uma vez (R$ 500,00).

### Variáveis globais
saldo = 0
extrato = ""
numero_saques = 0
Variáveis globais: Armazenam informações que serão usadas e atualizadas ao longo do programa.
saldo: Armazena o valor total de dinheiro na conta.
extrato: Guarda o histórico de transações (depósitos e saques).
numero_saques: Conta quantos saques já foram realizados.

### Funções
def exibir_menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    return input(menu)
Função exibir_menu(): Exibe o menu de opções para o usuário e retorna a opção escolhida.
Aqui, usamos a função input() para capturar a entrada do usuário.

def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
        
Função depositar(valor): Responsável por adicionar dinheiro à conta do usuário.
global saldo, extrato: Indica que estamos utilizando as variáveis saldo e extrato declaradas fora da função.
if valor > 0: Verifica se o valor do depósito é positivo.
saldo += valor: Atualiza o saldo da conta com o novo valor depositado.
extrato += ...: Adiciona a transação ao extrato.

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
        
Função sacar(valor): Responsável por retirar dinheiro da conta do usuário.
global saldo, numero_saques, extrato: Usa as variáveis saldo, numero_saques e extrato globais.
excedeu_saldo: Verifica se o valor do saque é maior que o saldo disponível.
excedeu_limite: Verifica se o valor do saque excede o limite permitido.
excedeu_saques: Verifica se o usuário já realizou o número máximo de saques permitidos.
if e elif: Várias verificações para garantir que o saque só ocorra se todas as condições forem cumpridas.

def exibir_extrato():
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    
Função exibir_extrato(): Mostra ao usuário o histórico de transações e o saldo atual.
if not extrato: Se não houver transações no extrato, uma mensagem indicando isso será exibida.
print(extrato): Exibe todas as transações realizadas.

### Loop principal
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
        
Loop principal: O programa roda continuamente até que o usuário escolha sair.
while True: Mantém o programa rodando indefinidamente até o break.
opcao = exibir_menu(): Captura a opção escolhida pelo usuário.
if e elif: Verifica qual operação o usuário escolheu e executa a função correspondente.
elif opcao == "q": Se o usuário escolher "q", o programa se encerra.
else: Se o usuário digitar uma opção inválida, uma mensagem de erro é exibida.
