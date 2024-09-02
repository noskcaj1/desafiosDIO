# 1-desafioDIO - Jackson Miranda

Programa de Banco em Python

### Introdução

Este conteúdo tem como objetivo explicar cada parte do programa de banco em Python.

### Constantes
Essas são variáveis cujo valor não muda durante a execução do programa.
 - LIMITE_SAQUES: Define o número máximo de saques permitidos por dia (3 saques).
 - LIMITE_SAQUE_VALOR: Define o valor máximo que pode ser sacado de uma vez (R$ 500,00).


![image](https://github.com/user-attachments/assets/44601837-c093-4a6e-ba2a-f25dbfaed42f)


### Variáveis globais:
Armazenam informações que serão usadas e atualizadas ao longo do programa.
 - saldo: Armazena o valor total de dinheiro na conta.
 - extrato: Guarda o histórico de transações (depósitos e saques).
 - numero_saques: Conta quantos saques já foram realizados.


![image](https://github.com/user-attachments/assets/65fe146e-0709-41bc-a3de-048396217a8c)


### Funções:
 - Função exibir_menu(): Exibe o menu de opções para o usuário e retorna a opção escolhida.
Aqui, usamos a função input() para capturar a entrada do usuário.


![image](https://github.com/user-attachments/assets/0759e1df-3680-487b-9441-71cb9d413063)


- Função depositar(valor): Responsável por adicionar dinheiro à conta do usuário.
    - global saldo, extrato: Indica que estamos utilizando as variáveis saldo e extrato declaradas fora da função.
    - if valor > 0: Verifica se o valor do depósito é positivo.
    - saldo += valor: Atualiza o saldo da conta com o novo valor depositado.
    - extrato += ...: Adiciona a transação ao extrato.

 
![image](https://github.com/user-attachments/assets/b31acebc-69e2-4ae5-920f-b032a28ba211)

        
- Função sacar(valor): Responsável por retirar dinheiro da conta do usuário.
    - global saldo, numero_saques, extrato: Usa as variáveis saldo, numero_saques e extrato globais.
    - excedeu_saldo: Verifica se o valor do saque é maior que o saldo disponível.
    - excedeu_limite: Verifica se o valor do saque excede o limite permitido.
    - excedeu_saques: Verifica se o usuário já realizou o número máximo de saques permitidos.
    - if e elif: Várias verificações para garantir que o saque só ocorra se todas as condições forem cumpridas.

 
![image](https://github.com/user-attachments/assets/46f7356b-b3ef-48d8-9148-4578a6a4bef4)

        
 - Função exibir_extrato(): Mostra ao usuário o histórico de transações e o saldo atual.
    - if not extrato: Se não houver transações no extrato, uma mensagem indicando isso será exibida.
    - print(extrato): Exibe todas as transações realizadas.
  

![image](https://github.com/user-attachments/assets/c03e52e7-424a-4597-a103-e9a613484cd7)


### Loop principal: 
O programa roda continuamente até que o usuário escolha sair.
- while True: Mantém o programa rodando indefinidamente até o break.
    - opcao = exibir_menu(): Captura a opção escolhida pelo usuário.
    - if e elif: Verifica qual operação o usuário escolheu e executa a função correspondente.
    - elif opcao == "q": Se o usuário escolher "q", o programa se encerra.
    - else: Se o usuário digitar uma opção inválida, uma mensagem de erro é exibida.

 
![image](https://github.com/user-attachments/assets/170dd9f8-ea70-4294-bfd8-3d7c4f06d8bd)



# 2º Desafio DIO

Visto que toda conta só pode ser aberta com cadastro de um CPF e todo usuario tem que possuir um CPF e endereço, decidi remover a opção de criação de usuários no menu principal e integrar essa lógica ao fluxo de criação de contas. Agora, ao tentar criar uma nova conta, o sistema irá verificar se o CPF já está cadastrado. Se o CPF não estiver cadastrado, o sistema perguntará se o usuário deseja criar um novo usuário. Caso o CPF já esteja cadastrado, o sistema confirmará se deseja continuar com a criação da nova conta ou cancelar a operação.

![image](https://github.com/user-attachments/assets/9b3844f5-f987-409f-b36e-cbbd2da55daf)
