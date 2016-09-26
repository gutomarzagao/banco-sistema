from conta import Conta

conta_logada = None
contas = []

while (True):
    comando = input("Digite um comando:")
    print(comando)
    if comando == 'deposito' and conta_logada != None:
        valor = int(input("Valor do depósito:"))
        conta_logada.depositar(valor)

    elif comando == 'saque' and conta_logada != None:
        valor = int(input("Valor do saque:"))
        conta_logada.sacar(valor)

    elif comando == 'saldo' and conta_logada != None:
        conta_logada.exibir_saldo()
        print (conta_logada.numero)

    elif comando == 'extrato' and conta_logada != None:
        conta_logada.exibir_extrato()

    elif comando == 'sair' and conta_logada != None:
        conta_logada = None

    elif comando == 'entrar' and conta_logada == None:
        numero_conta = int(input("digite o numero da sua conta"))
        for conta in contas:
            if conta.numero == numero_conta:
                conta_logada = conta

        if conta_logada == None:
            conta_logada = Conta(numero_conta)
            contas.append(conta_logada)
        print("Bem vindo a sua conta")

    elif comando == 'fechar':
        exit()
    else:
        print("comando inexistente")
