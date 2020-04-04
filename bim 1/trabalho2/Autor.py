class Autor:
    def __init__(self, nome, email):
        self._nome = nome
        self._email = email
        self._cod = None
    @property
    def nome(self):
        return self._nome 
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @property
    def cod(self):
        return self._cod
    @cod.setter 
    def cod(self, cod):
        self._cod = cod
    
    @property
    def email(self):
        return self._email
    @email.setter 
    def email(self, email):
        self._email = email
    
    def __str__(self): 
        s = "Código:{}, Nome:{}, E-mail:{}".format(self._cod, self._nome, self._email)
        return s     