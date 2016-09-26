from conta import Conta
conta1 = Conta()
# aqui comeca o codigo de verdade
comando = input("faça login:")
print(comando)
if comando == 'entrar':
    print("Bem vindo a sua conta")
    while (True):
        comando = input("Digite um comando:")
        print(comando)
        if comando == 'deposito':
            valor = int(input("Valor do depósito:"))
            conta1.depositar(valor)

        elif comando == 'saque':
            valor = int(input("Valor do saque:"))
            conta1.sacar(valor)

        elif comando == 'saldo':
            conta1.exibir_saldo()

        elif comando == 'extrato':
            conta1.exibir_extrato()
        elif comando == 'sair':
            break
        else:
            print("comando inexistente")
elif comando == 'fechar':
    exit()
else:
    print("faca o login para fazer operacoes")