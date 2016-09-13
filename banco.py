comando = ""
saldo=[0]
while (True):
    comando = input("Digite um comando:")
    print(comando)
    if(comando=="deposito"):
        depositar=int(input("Valor do depósito:"))
        if(depositar<0):
            print("nao aceitamos depositos negativos")
        else:
            saldo.append(depositar)
    elif(comando=="saque"):
        sacar=int(input("Valor que deseja sacar:"))
        if(sacar<0):
            print("nao aceitamos saques negativos")
        else:
            saldo.append(-sacar)
    elif(comando=="saldo"):
        print("seu saldo é", sum(saldo))
    elif(comando=="sair"):
        exit()
    elif(comando!=['sair', 'saldo', 'saque', 'deposito']):
        print("comando inexistente")
    else: break