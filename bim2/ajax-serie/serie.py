class Serie:
    def __init__(self,**kwargs):
        if(kwargs.get("cod")): self._cod = kwargs["cod"]
        if(kwargs.get("titulo")): self._titulo = kwargs["titulo"]
    
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
    def titulo(self,titulo):
        self._titulo = titulo 