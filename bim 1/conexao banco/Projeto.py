from psycopg2 import connect
from datetime import datetime
class Projeto:
    def __init__(self, nome, data):
        self._cod = None
        self._nome = nome
        self._data = data

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
    def data(self):
        return self._data
    @data.setter 
    def data(self, data):
        self._data = data
