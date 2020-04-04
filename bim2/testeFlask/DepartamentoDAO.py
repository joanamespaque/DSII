import psycopg2
from psycopg2 import connect
from datetime import datetime
from Departamento import Departamento
from FuncionarioDAO import *
from ProjetoDAO import *

class DepartamentoDAO:
    def __init__(self):
        self._con = 'dbname=aula1 user=postgres password=postgres host=localhost port=5432'

    def listar(self):
        vet = []
        try:
            with connect(self._con) as com:
                cur = com.cursor()
                cur.execute("SELECT * FROM departamento")
                # print(cur.fetchall())
                daof = FuncionarioDAO()
                for linha in cur.fetchall():
                    dep = Departamento(linha[1])
                    dep.cod = linha[0]
                    dep.dt_atu = linha[2]
                    dep.gerente = daof.buscar(linha[3])
                    vet.append(dep) #!!!!!!!!!!!!!!!!!!!!!
                cur.close()
                return vet
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")

    def buscar(self, cod):
        try:
            with connect(self._con) as conn:
                cur = conn.cursor()
                cur.execute("SELECT d.codigo, d.nome, d.dt_atu, d.codgerente, f.nome as gerente	FROM departamento d INNER JOIN funcionario f ON d.codgerente = f.codigo WHERE d.codigo = %s", [cod])
                linha = cur.fetchall()
                print(linha)
                departamento = Departamento(linha[0][1])
                departamento.cod = linha[0][0]
                departamento.dt_atu = linha[0][2]
                dao = FuncionarioDAO()
                departamento.gerente = dao.buscar(linha[0][3]) 
                conn.commit()
                cur.close()
                # return linha[0][0]
                return departamento
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")

    def inserir(self, departamento):
        try:
            with connect(self._con) as conn:
                cur = conn.cursor()
                sql = cur.execute("INSERT INTO departamento (nome, dt_atu, codgerente) VALUES (%s, now(), %s) returning codigo, dt_atu", [departamento.nome, departamento.gerente.cod])
                linha = cur.fetchone()
                daoF = FuncionarioDAO()
                departamento.cod = linha[0]
                departamento.dt_atu = linha[1]
                # print(cur.query)
                conn.commit()
                cur.close()
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")
    
    def excluir(self, cod):
        try:
            with connect(self._con) as conn:
                cur = conn.cursor()
                sql = cur.execute("DELETE FROM departamento WHERE codigo=%s", [cod])
                conn.commit() 
                cur.close()
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")

    def salvar(self, departamento):
        dao = DepartamentoDAO()
        if(departamento.cod==None):
            dao.inserir(departamento)
        else:
            dao.alterar(departamento)
    
    def alterar(self, departamento):
        try: 
            with connect(self._con) as conn:
                cur = conn.cursor()
                sql = cur.execute("UPDATE departamento SET nome = %s, dt_atu = now(), codgerente = %s WHERE codigo = %s",[departamento.nome, departamento.gerente.cod, departamento.cod])
                conn.commit()
                cur.close
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")
        


if (__name__ == '__main__'):
    dao = DepartamentoDAO()
    daoF = FuncionarioDAO()
    # dep = Departamento("mudaTESTE")
    # dep.cod = 5
    # dep1 = Departamento("teste")
    # dep1 = Departamento("alo celso")
    # dao.inserir(dep1)
    # dao.excluir(7)
    
    # gerente = daoF.buscar(2)
    # departamento = Departamento("pipoca")
    # departamento.gerente = gerente
    # dao.inserir(departamento)
    # print(dao.buscar(3))
    # print(dao.listar())
    # dao.alterar(dep)
    # novogerente = dao.buscar(3)
    # depto2 = Departamento("TesteAlterar")
    # depto2.cod = 5
    # depto2.gerente = novogerente 
    # dao.alterar(depto2)
    # print(dao.buscar(5))
    # lista = dao.listar() 
    # for d in lista:
    #     print(d)
