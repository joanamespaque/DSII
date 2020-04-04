from psycopg2 import connect
from datetime import datetime
# from Departamento import Departamento
class Funcionario: 
    def __init__(self, nome, login, senha=None, adm=False):
        self._nome = nome
        self._login = login 
        self._senha = senha
        self._cod = None
        self._adm = adm
        self._departamento = None

    @property
    def adm(self):
        return self._adm
    @adm.setter
    def adm(self, adm):
        self._adm = adm
    # def ehadm():
    #     self._adm = True

    @property
    def login(self):
        return self._login  
    @login.setter 
    def login(self, login):
        self._login = login

    @property
    def senha(self):
        return self._senha  
    @senha.setter 
    def senha(self, senha):
        self._senha = senha

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
        return "Código:{} Nome:{} Login:{} ADM:{} CodDepartamento:{} NomeDepartamento:{} DataAtualizaçãoDepto:{}".format(str(self._cod), self._nome, self._login, self._adm, str(self._departamento.cod), self._departamento.nome, self._departamento.dt_atu)
