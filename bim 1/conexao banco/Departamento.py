import datetime
from Funcionario import Funcionario
class Departamento: 
    def __init__(self, nome):
        self._nome = nome
        self._cod = None
        self._dt_atu = None    
        self._gerente = None 
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
    def dt_atu(self):
        return self._dt_atu
    @dt_atu.setter 
    def dt_atu(self, dt):
        self._dt_atu = dt

    @property
    def gerente(self):
        return self._gerente 
    @gerente.setter
    def gerente(self, gerente):
        self._gerente = gerente 
    

    def __str__(self): 
        if(self.gerente):
            s = "Código:{}, Nome:{}, Data de Atualização:{}, CodGerente:{}".format(str(self._cod), self._nome, self._dt_atu.strftime("%d/%m/%Y"), self._gerente.cod)
        else:
            s = "Código:{}, Nome:{}, Data de Atualização:{}".format(str(self._cod), self._nome, self._dt_atu.strftime("%d/%m/%Y"))   
        return s     


    
