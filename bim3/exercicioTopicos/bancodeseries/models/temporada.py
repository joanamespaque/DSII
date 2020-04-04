class Temporada:
    def __init__(self,**kwargs):
        if(kwargs.get("cod")): self._cod = kwargs["cod"]
        if(kwargs.get("titulo")): self._titulo = kwargs["titulo"]
        if(kwargs.get("serie")): self._serie = kwargs["serie"]
        if(kwargs.get("numero")): self._numero = kwargs["numero"]
        
    @property
    def cod(self):
        return self._cod
    @cod.setter
    def cod(self, cod):
        self._cod = cod

    @property
    def titulo(self):
        return self._titulo
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def numero(self):
        return self._numero
    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def serie(self):
        return self._serie
    @serie.setter
    def serie(self,serie):
        self._serie = serie


    def toDict(self):
        dict = {
            "cod": self._cod,
            "titulo": self._titulo,
            "numero": self._numero,
            "serie": {
                "cod": self._serie.cod,
                "titulo": self._serie.titulo,
            }
        }
        return dict 

    def persistido(self):
        return hasattr(self,"_cod") and self.cod!=None 
