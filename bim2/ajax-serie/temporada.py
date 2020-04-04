class Temporada:
    def __init__(self,**kwargs):
        if(kwargs.get("cod")): self._cod = kwargs["cod"]
        if(kwargs.get("numero")): self._numero = kwargs["numero"]
        if(kwargs.get("serie")): self._serie = kwargs["serie"]
        
    @property
    def cod(self):
        return self._cod
    @cod.setter
    def cod(self, cod):
        self._cod = cod

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