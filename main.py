from conta import Conta

conta1 = Conta()
logado = False

while (True):
    comando = input("Digite um comando:")
    print(comando)
    if comando == 'deposito' and logado:
        valor = int(input("Valor do depósito:"))
        conta1.depositar(valor)

    elif comando == 'saque' and logado:
        valor = int(input("Valor do saque:"))
        conta1.sacar(valor)

    elif comando == 'saldo' and logado:
        conta1.exibir_saldo()

    elif comando == 'extrato' and logado:
        conta1.exibir_extrato()
    elif comando == 'sair' and logado:
        logado = False
    elif comando == 'entrar' and not logado:
        print("Bem vindo a sua conta")
        logado = True
    elif comando == 'fechar':
        exit()
    else:
        print("comando inexistente")
