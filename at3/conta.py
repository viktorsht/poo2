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

    _total_contas = 0
    __slots__ = ['_numero','_titular','_saldo','_limite']


    def __init__(self, numero,titular, saldo,limite):
        self._titular = titular
        self._saldo = saldo
        self._numero = numero
        self._limite = limite
        self.historico = Historico()
        Conta._total_contas += 1

    @property
    def saldo(self):
        return self._saldo

    @property
    def titular(self):
        return self._titular

    @property
    def numero(self):
        return self._numero

    @property
    def limite(self):
        return self._limite

    @titular.setter
    def titular(self,titular):
        self._titular = titular

    @numero.setter
    def numero(self,numero):
        self._numero = numero

    @limite.setter
    def limite(self,limite):
        self._limite = limite

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            print("Valor do saldo não pode ser negativo")
        else:
            self._saldo = valor

    def extrato(self):
        self.titular.imprimir()
        print('Numero = ', self.numero)
        print('Saldo = ', self._saldo)
        #print('Limite = ', self.limite)

    def mostrarHistorico(self):
        self.historico.imprimir()

    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            self.historico.transacoes.append('Saque de {} reais realizado com sucesso!'.format(valor))
            return True
        else:
            self.historico.transacoes.append('Tentativa de saque recusada!')
            return False

    def depositar(self, valor):
        if valor < 0:
            return False
        else:
            self._saldo += valor
            return True

    def transferir(self, destino, valor):
        retorno = self.sacar(valor)
        if retorno == True:
            destino.depositar(valor)
        else:
            return False

    def atualiza(self,taxa):
        self._saldo += self._saldo * taxa

    def __str__(self,numero,titular, saldo):
        return "{}\n{}\n{}".format(self._titular,self.numero,self._saldo)

    @staticmethod
    def get_total_contas():
        return Conta._total_contas



if __name__ == '__main__':
    c1 = Conta(1,'vitor',100.0,1000.0)
    c2 = Conta(1,'vitor',100.0,1000.0)
    print(c1.get_total_contas())
