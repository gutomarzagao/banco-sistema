class Conta:
    extrato = []
    saldo = 0
    operacao = []

    def exibir_saldo(self):
        print("seu saldo é", self.saldo)

    def exibir_extrato(self):
        for x,y in zip(self.extrato,self.operacao):
            print (y,x)

    def depositar(self, valor):
        if valor < 0:
            print('nao aceitamos depositos negativos.')
        else:
            self.extrato.append(valor)
            self.operacao.append("deposito")
            self.saldo += valor

    def sacar(self, valor):
        if (valor < 0):
            print("nao aceitamos saques negativos.")
        elif (valor > self.saldo):
            print("saque maior que saldo, operacao nao realizada.")
        else:
            self.extrato.append(-valor)
            self.operacao.append("saque")
            self.saldo -= valor
