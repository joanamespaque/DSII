from psycopg2 import connect
from datetime import datetime
from FuncionarioDAO import *
class Projeto:
    def __init__(self, nome, dataprevista):
        self._cod = None
        self._nome = nome
        self._dataprevista = dataprevista
        self._funcionarios = []
    def desvinculaFuncionario(self, funcionario):
        i = 0
        while i < len(self._funcionarios):
            if(self._funcionarios[i].cod == funcionario.cod):
                del(self._funcionarios[i])
                break
            i+=1

    def vinculaFuncionario(self, funcionario):
        codigos = []
        for f in self._funcionarios:
            codigos.append(f.cod)
        if(not codigos.__contains__(funcionario.cod)):
            self._funcionarios.append(funcionario)
        # daoF = FuncionarioDAO()
        # lista = daoF.listar()
        # for func in lista:
        #     if(func.cod == funcionario.cod):
        #         self._funcionarios.append(funcionario)

    @property
    def funcionarios(self):
        return self._funcionarios 

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
    def dataprevista(self):
        return self._dataprevista
    @dataprevista.setter 
    def dataprevista(self, dataprevista):
        self._dataprevista = dataprevista

    def __str__(self): 
        array = []
        for f in self.funcionarios:
            funcionario = "Código:{}, Nome:{}, Login:{}, ADM:{}".format(f.cod, f.nome, f.login, f.adm)
            array.append([funcionario])
        # print(array) FUNCIONA
        return "Código:{} Nome:{} Data Prevista:{} \nFuncionário(s) vinculado(s):{}".format(str(self._cod), self._nome, self._dataprevista, array)
