from psycopg2 import connect
from datetime import datetime
from Departamento import Departamento
from FuncionarioDAO import *

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
                for linha in cur.fetchall():
                    dep = Departamento(linha[1])
                    dep.cod = linha[0]
                    dep.dt_atu = linha[2]
                    vet.append(dep) #!!!!!!!!!!!!!!!!!!!!!
                cur.close()
                return vet
        except BaseException as e: 
            print("treta")
            raise e

    def buscar(self, cod):
        try:
            with connect(self._con) as conn:
                cur = conn.cursor()
                cur.execute("SELECT d.codigo, d.nome, d.dt_atu, d.codgerente, f.nome as gerente	FROM departamento d INNER JOIN funcionario f ON d.codgerente = f.codigo WHERE d.codigo = %s", [cod])
                linha = cur.fetchall()
                # print(linha)
                departamento = Departamento(linha[0][1])
                departamento.cod = linha[0][0]
                departamento.dt_atu = linha[0][2]
                dao = FuncionarioDAO()
                departamento.gerente = dao.buscar(linha[0][3]) 
                conn.commit()
                cur.close()
                # return linha[0][0]
                return departamento
        except Exception as e:
            print("Treta")
            raise e

    def inserir(self, departamento):
        try:
            with connect(self._con) as conn:
                cur = conn.cursor()
                sql = cur.execute("INSERT INTO departamento (nome, dt_atu, codgerente) VALUES (%s, now(), %s)", [departamento.nome, departamento.gerente.cod])
                # print(cur.query)
                conn.commit()
                cur.close()
        except Exception as e:
            print("treta")
            raise e
    
    def excluir(self, cod):
        try:
            with connect(self._con) as conn:
                cur = conn.cursor()
                sql = cur.execute("DELETE FROM departamento WHERE codigo=%s", str(cod))
                conn.commit() 
                cur.close()
        except Exception as e:
            print("Treta")
            raise e 
    
    def alterar(self, departamento):
        try: 
            with connect(self._con) as conn:
                cur = conn.cursor()
                sql = cur.execute("UPDATE departamento SET nome = %s, dt_atu = now(), codgerente = %s WHERE codigo = %s",[departamento.nome, departamento.gerente.cod, departamento.cod])
                conn.commit()
                cur.close
        except Exception as e:
            print("TRETA")
            raise e
	
        


# if (__name__ == '__main__'):
#     dao = DepartamentoDAO()
#     daoF = FuncionarioDAO()
#     # dep = Departamento("mudaTESTE")
#     # dep.cod = 5
#     # dep1 = Departamento("teste")
#     # dep1 = Departamento("alo celso")
#     # dao.inserir(dep1)
#     # dao.excluir(7)
    
#     # gerente = daoF.buscar(2)
#     # departamento = Departamento("pipoca")
#     # departamento.gerente = gerente
#     # dao.inserir(departamento)
#     # print(dao.buscar(3))
#     # print(dao.listar())
#     # dao.alterar(dep)
#     # novogerente = dao.buscar(3)
#     # depto2 = Departamento("TesteAlterar")
#     # depto2.cod = 5
#     # depto2.gerente = novogerente 
#     # dao.alterar(depto2)
#     print(dao.buscar(4))
#     lista = dao.listar() 
#     for d in lista:
#         print(d)
