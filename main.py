import conta

extrato=[0]
saldo=0
def comandar(x):
    comando == x
    return
def exibir_saldo():
    print("seu saldo é", saldo)
    return

def exibir_extrato():
    return

def sacar():
    return

def depositar():
    return
while (True):
    comando = input("Digite um comando:")
    print(comando)

    if comando=="deposito":
        depositar=int(input("Valor do depósito:"))
        if depositar<0:
            print('nao aceitamos depositos negativos.')
        else:
            extrato.append(depositar)
            saldo += depositar

    elif comando== "saque":
        sacar=int(input("Valor que deseja sacar:"))
        if(sacar<0):
            print("nao aceitamos saques negativos.")
        elif sacar>saldo:
            print("saque maior que saldo, operacao nao realizada.")
        else:
            extrato.append(-sacar)
            saldo -= sacar

    elif comandar('saldo'):
        exibir_saldo()

    elif comando == "extrato":
        for k,v in enumerate(extrato):
            print(k, v)
    elif comando== "sair":
        break
    else:
        print("comando inexistente")