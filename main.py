extrato=[]
saldo=0
operacao = []

# aqui comecam as funcoes
def comandar(x):
    return comando == x
def exibir_saldo():
    print("seu saldo é", saldo)

def exibir_extrato():
    for x,y in zip(extrato,operacao):
        print (y,x)

def depositar():
    global saldo
    depositar = int(input("Valor do depósito:"))
    if depositar < 0:
        print('nao aceitamos depositos negativos.')
    else:
        extrato.append(depositar)
        operacao.append("deposito")
        saldo += depositar
def sacar():
    global saldo
    sacar = int(input("Valor que deseja sacar:"))
    if (sacar < 0):
        print("nao aceitamos saques negativos.")
    elif (sacar > saldo):
        print("saque maior que saldo, operacao nao realizada.")
    else:
        extrato.append(-sacar)
        operacao.append("saque")
        saldo -= sacar

# aqui comeca o codigo de verdade
while (True):
    comando = input("Digite um comando:")
    print(comando)
    if comandar('entrar'):
        print("Bem vindo a sua conta")
        while (True):
            comando = input("Digite um comando:")
            print(comando)
            if comandar('deposito'):
                depositar()

            elif comandar('saque'):
                sacar()

            elif comandar('saldo'):
                exibir_saldo()

            elif comandar('extrato'):
                exibir_extrato()
            elif comandar('sair'):
                break
            else:
                print("comando inexistente")
    elif comandar('fechar'):
        break
    else:
        print("faca o login para fazer operacoes")