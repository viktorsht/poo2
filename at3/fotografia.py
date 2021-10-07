from matplotlib.pyplot import imshow
from skimage.io import imread

class Pessoa:

    __slots__ = ['_nome', '_cpf', '_endereco', '_telefone']

    def __init__(self, nome, cpf, endereco, telefone):
        self._nome = nome
        self._cpf = cpf
        self._endereco = endereco
        self._telefone = telefone

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def endereco(self):
        return self._endereco

    @property
    def telefone(self):
        return self._telefone

    @nome.setter
    def nome(self,nome):
        self._nome = nome

    @cpf.setter
    def cpf(self,cpf):
        self._cpf = cpf

    @endereco.setter
    def endereco(self,endereco):
        self._endereco = endereco

    @telefone.setter
    def telefone(self,telefone):
        self._telefone = telefone


class Fotografia:

    __slots__ = ['_foto','_fotografo','_data','_proprietario','_qtd_fotos']

    def __init__(self,foto,fotografo,data,proprietario,qtd_fotos):
        self._foto = foto
        self._fotografo = fotografo
        self._data = data
        self._proprietario = proprietario
        self._qtd_fotos = qtd_fotos

    @property
    def foto(self):
        return self._foto

    @property
    def fotografo(self):
        return self._fotografo

    @property
    def data(self):
        return self._data

    @property
    def proprietario(self):
        return self._proprietario

    @property
    def qtd_fotos(self):
        return self._qtd_fotos

    @foto.setter
    def foto(self,foto):
        self._foto = foto

    @fotografo.setter
    def fotografo(self,fotografo):
        self._fotografo = fotografo

    @data.setter
    def data(self,data):
        self._data = data

    @foto.setter
    def qtd_fotos(self,qtd_fotos):
        self._qtd_fotos = qtd_fotos

    def mostrar_fotografia(self):
         img = imread(self._foto)
         imshow(img)

    def propriedades_foto(self):
        #return fotografia.shape
        pass

    def tamanho_fotografia(self):
        img = imread(self._foto)
        return f\"resolução da imagem: {img.shape[1]} x {img.shape[0]} pixels\"

    @property
    def fotografo(self) -> Pessoa:
        return self._fotografo

    @property
    def proprietario(self) -> Pessoa:
        return self._proprietario

    @property
    def data(self)
        return self._data

    @staticmethod
    def total_fotos()
        return Fotografia._qtd_fotos

if __name__ == '__main__':
    foto = 'foto2.jpeg'
    fotografo = 'oi'
    data = '16/09/2021'
    proprietario = fotografo
    qtd_fotos = 0
    f = Fotografia(foto,fotografo,data,proprietario,qtd_fotos)
    f.mostrar_fotografia()
