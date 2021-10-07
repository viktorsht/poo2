class Cadastro:

    __slots__ = ['_lista_pessoas']
    def __init__(self):
        self._lista_pessoas = []

    def cadastra(self,pessoa):
        existe = self.busca(pessoa.cpf)
        if(existe == None):
            self._lista_pessoas.append(pessoa)
            return True
        else:
            return False

    def busca(self,cpf):
        for lp in self._lista_pessoas:
            if lp.cpf == cpf:
                return lp
        return None


'''

from PyQt5.QtWidgets import QMessageBox
from cadastro import Cadastro
from pessoa import Pessoa

    self.cad = Cadastro()
    self.pushButton.clicked.connect(self.botaoCadastra)
    self.pushButton_2.clicked.connect(self.botaoBusca)

def botaoCadastra(self):
    nome = self.lineEdit.text()
    endereco = self.lineEdit_2.text()
    cpf = self.lineEdit_3.text()
    nascimento = self.lineEdit_4.text()
    if not(nome == '' or endereco == '' or cpf == '' or nascimento == ''):
        p = Pessoa(nome,endereco,cpf,nascimento)
        if( self.cad.cadastra(p)):
            QMessageBox.information(None,' [ ! ]','Sucesso!')
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
            self.lineEdit_3.setText('')
            self.lineEdit_4.setText('')
        else:
            QMessageBox.information(None,' [ ! ]','CPF já existe!')
    else:
            QMessageBox.information(None,' [ ! ]','DADOS INCORRETOS')

def botaoBusca(self):
    cpf = self.lineEdit_5.text()
    pessoa = self.cad.busca(cpf)
    if( pessoa != None):
        self.lineEdit_6.setText(pessoa.nome)
        self.lineEdit_7.setText(pessoa.endereco)
        self.lineEdit_8.setText(pessoa.nascimento)
    else:
        QMessageBox.information(None,' [ ! ]','CPF NÂO ENCONTRADO!')




'''
