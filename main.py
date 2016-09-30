from conta import Conta
import json

conta_logada = None
contas = []

def converter_lista_json(obj):
    return obj.__dict__

while (True):

    comando = input("Digite um comando:")
    print(comando)
    if comando == 'sair' and conta_logada != None:
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
        with open('dados.txt', 'w') as dados:
            json.dump(contas, dados, default=converter_lista_json)
        exit()
    elif comando == 'deposito' and conta_logada != None:
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

    elif comando == 'transferencia' and conta_logada != None:
        if conta_logada.saldo <= 0:
            print("Voce não tem saldo para transferencias")
        else:
            valor_transf = int(input("Valor da transferencia:"))
            if valor_transf > 0 and valor_transf <= conta_logada.saldo:
                conta_transf = int(input("conta de destino:"))
                if conta_transf == conta.numero:
                    conta_logada.saldo = conta_logada.saldo - valor_transf
                    conta_transf = conta
                    conta_transf.saldo = conta_transf.saldo + valor_transf
                else:
                    print("conta inexistente")
            else:
                print("so pode transferir valores positivos")
    else:
        print("comando inexistente")
