class Serie:
    def __init__(self,**kwargs):
        if(kwargs.get("cod")): self._cod = kwargs["cod"]
        if(kwargs.get("titulo")): self._titulo = kwargs["titulo"]
        if(kwargs.get("usuario")): self._usuario = kwargs["usuario"]
        if(kwargs.get("foto")): self._foto = kwargs["foto"]
    
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
    def usuario(self):
        return self._usuario
    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario 

    @property
    def foto(self):
        return self._foto
    @foto.setter
    def foto(self, foto):
        if type(foto) != str and foto is not None:
            raise ValueError()
        self._foto = foto
        
    def persistido(self):
        return hasattr(self,"_cod") and self.cod!=None 