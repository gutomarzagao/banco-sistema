comando = ""
extrato=[0]
saldo=0
depositar=int()
while (True):
    comando = input("Digite um comando:")
    print(comando)
    if(comando=="deposito"):
        depositar=int(input("Valor do depósito:"))
        if(depositar<0):
            print("nao aceitamos depositos negativos.")
        else:
            extrato.append(depositar)
            saldo += depositar
    elif(comando=="saque"):
        sacar=int(input("Valor que deseja sacar:"))
        if(sacar<0):
            print("nao aceitamos saques negativos.")
        elif(sacar>saldo):
            print("saque maior que saldo, operacao nao realizada.")
        else:
            extrato.append(-sacar)
            saldo -= sacar
    elif(comando=="saldo"):
        print("seu saldo é", saldo)
    elif(comando=="sair"):
        break
    else:
        print("comando inexistente")