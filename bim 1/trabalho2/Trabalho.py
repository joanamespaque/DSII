from datetime import datetime
class Trabalho:
    def __init__(self, titulo, conteudo, nota):
        self._conteudo = conteudo 
        self._nota = nota
        self._titulo = titulo
        self._cod = None
        self._dataEntrega = None
        self._dataHoraAtualizacao = None
        self._autores = []
    @property
    def autores(self):
        return self._autores
    
    def vinculaAutor(self, autor):
        self._autores.append(autor)
    
    @property
    def conteudo(self):
        return self._conteudo 
    @conteudo.setter
    def conteudo(self, conteudo):
        self._conteudo = conteudo

    @property
    def nota(self):
        return self._nota 
    @nota.setter
    def nota(self, nota):
        self._nota = nota

    @property
    def titulo(self):
        return self._titulo 
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def cod(self):
        return self._cod 
    @cod.setter
    def cod(self, cod):
        self._cod = cod

    @property
    def dataEntrega(self):
        return self._dataEntrega 
    @dataEntrega.setter 
    def dataEntrega(self, dataEntrega): 
        self._dataEntrega = dataEntrega

    def entregaTrabalho(self):
        self._dataEntrega = datetime.now()
    
    @property
    def dataHoraAtualizacao(self):
        return self._dataHoraAtualizacao 
    @dataHoraAtualizacao.setter
    def dataHoraAtualizacao(self, dataHoraAtualizacao):
        self._dataHoraAtualizacao = dataHoraAtualizacao

    def __str__(self): 
        newVetor = []
        for a in self.autores:
            autor = "Nome:{}, Email:{}".format(a.nome, a.email)
            newVetor.append(autor)
        s = "Código:{}, Título:{}, Conteúdo:{}, Nota:{}, DataEntrega:{}, DataHoraAtualização:{}, Autores:{}".format(str(self.cod), self.titulo, self.conteudo, self.nota, self.dataEntrega,self.dataHoraAtualizacao, newVetor)
        return s    