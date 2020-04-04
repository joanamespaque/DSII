from datetime import datetime
# from Departamento import Departamento
class Funcionario: 
    def __init__(self, nome):
        self._nome = nome
        self._cod = None
        self._departamento = None

    @property
    def nome(self):
        return self._nome 
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def departamento(self):
        return self._departamento
    @departamento.setter
    def departamento(self, departamento):
        self._departamento = departamento 
    
    @property
    def cod(self):
        return self._cod
    @cod.setter 
    def cod(self, cod):
        self._cod = cod 
    
    def __str__(self): 
        return "Código:{} Nome:{} CodDepartamento:{} NomeDepartamento:{} DataAtualizaçãoDepto:{}".format(str(self._cod), self._nome, str(self._departamento.cod), self._departamento.nome, self._departamento.dt_atu)
