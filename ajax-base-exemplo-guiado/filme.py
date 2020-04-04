class Filme:
    def __init__(self,**kwargs):
        if(kwargs.get("id")): self._id = kwargs["id"]
        if(kwargs.get("titulo")): self._titulo = kwargs["titulo"]
        if(kwargs.get("direcao")): self._direcao = kwargs["direcao"]
        if(kwargs.get("genero")): self._genero = kwargs["genero"]
        if(kwargs.get("duracao")): self._duracao = kwargs["duracao"]
        if(kwargs.get("sinopse")): self._sinopse = kwargs["sinopse"]
        if(kwargs.get("elenco")): self._elenco = kwargs["elenco"]
        if(kwargs.get("dataLancamento")): self._dataLancamento = kwargs["dataLancamento"]
        if(kwargs.get("classificacao")): self._classificacao = kwargs["classificacao"]

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def titulo(self):
        return self._titulo
    @titulo.setter
    def titulo(self,titulo):
        self._titulo = titulo 

    @property
    def direcao(self):
        return self._direcao 
    @direcao.setter
    def direcao(self, direcao):
        self._direcao = direcao

    @property
    def genero(self):
        return self._genero
    @genero.setter 
    def genero(self, genero):
        self._genero = genero

    @property
    def duracao(self):
        return self._duracao
    @duracao.setter 
    def duracao(self, duracao):
        self._duracao = duracao
    
    @property
    def sinopse(self):
        return self._sinopse
    @sinopse.setter
    def sinopse(self, sinopse):
        self._sinopse = sinopse
    
    @property
    def elenco(self):
        return self._elenco
    @elenco.setter 
    def elenco(self, elenco):
        self._elenco = elenco

    @property
    def dataLancamento(self):
        return self._dataLancamento
    @dataLancamento.setter
    def dataLancamento(self, data):
        self._dataLancamento = data

    @property
    def classificacao(self):
        return self._classificacao
    @classificacao.setter
    def classificacao(self, classificacao):
        self._classificacao = classificacao

    def toDict(self):
        dict = {
            "id": self._id,
            "titulo": self._titulo,
            "direcao": self._direcao,
            "genero": self._genero, 
            "duracao": self._duracao.strftime('%H:%M:%S'),
            "sinopse": self._sinopse,
            "elenco": self._elenco,
            "dataLancamento": self._dataLancamento.strftime('%d/%m/%Y'),
            "classificacao": self._classificacao
        }
        return dict   
    