import datetime as dt

class Historico:

    def __init__(self):
        self.data_abertura = dt.datetime.today()
        self.transacoes = []

    def imprimir(self):
        print('Data de abertura da conta = ', self.data_abertura)
        for i in self.transacoes:
            print(i)

class Conta(Historico):

    def __init__(self, numero,titular, saldo,limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
	    self.historico = Historico()


    def depositar(self, valor):
        if valor < 0:
            return False
            self.historico.transacoes.append('Saldo Insuficiente!')
        else:
            self.saldo += valor
            self.historico.transacoes.append('Deposito de {} reais realizado com sucesso!'.format(valor))
            return True

    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            self.historico.transacoes.append('Saque de {} reais realizado com sucesso!'.format(valor))
            return True
        else:
            self.historico.transacoes.append('Tentativa de saque recusada!')
            return False

    def extrato(self):
        print('Numero = ', self.numero)
        print('Titular = ', self.titular)
        print('Saldo = ', self.saldo)
        print('Limite = ', self.limite)

    def transferir(self, destino, valor):
        retorno = self.sacar(valor)
        if retorno == True:
            destino.depositar(valor)
            self.historico.transacoes.append('Tranferencia de {} reais realizada com sucesso!'.format(valor))
        else:
            self.historico.transacoes.append('Tentativa de saque recusada!')
            return False

class Cliente:

    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


if __name__ == '__main__':
	c = Conta(100,'vitor',1000,2000)
	c.depositar(1000)
