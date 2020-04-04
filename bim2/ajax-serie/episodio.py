class Episodio:
    def __init__(self,**kwargs):
        if(kwargs.get("cod")): self._cod = kwargs["cod"]
        if(kwargs.get("titulo")): self._titulo = kwargs["titulo"]
        if(kwargs.get("serie")): self._serie = kwargs["serie"]
        if(kwargs.get("temporada")): self._temporada = kwargs["temporada"]
    
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

    @property
    def serie(self):
        return self._serie
    @serie.setter
    def serie(self, serie):
        self._serie = serie

    @property
    def temporada(self):
        return self._temporada
    @temporada.setter
    def temporada(self,temporada):
        self._temporada = temporada 