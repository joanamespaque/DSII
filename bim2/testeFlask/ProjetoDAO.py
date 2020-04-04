from FuncionarioDAO import *
from Projeto import Projeto 
from datetime import datetime
import psycopg2
class ProjetoDAO:
    def __init__(self):
        self._con = 'dbname=aula1 user=postgres password=postgres host=localhost port=5432'
    def inserir(self, projeto):
        try:
            with connect(self._con) as conn:
                cur = conn.cursor()
                sql = cur.execute('INSERT INTO projeto (nome, dataprevista) VALUES (%s, %s)returning codigo', [projeto.nome, projeto.dataprevista])
                linha = cur.fetchone()
                projeto.cod = linha[0]
                conn.commit()
                cur.close()
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")
    def excluir(self, cod): 
        try:
            with connect(self._con) as conn:
                cur = conn.cursor()
                sql = cur.execute("DELETE FROM projeto WHERE codigo=%s", [cod])
                conn.commit() 
                cur.close()
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")

    def alterar(self, projeto):
        try:
            with connect(self._con) as conn:
                cur = conn.cursor()
                sql = cur.execute('UPDATE projeto SET nome=%s, dataprevista=%s WHERE codigo = %s ', [projeto.nome, projeto.dataprevista, projeto.cod]) 
                conn.commit()
                cur.close()
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")

    def buscar(self, cod): 
        try:
            with connect(self._con) as con:
                cur = con.cursor()
                cur.execute('SELECT p.codigo, p.nome, p.dataprevista, f.codigo AS codFunc, f.nome, f.login, d.nome FROM projeto p LEFT JOIN funcproj fp ON p.codigo =  fp.codigoprojeto LEFT JOIN funcionario f ON f.codigo = fp.codigofuncionario LEFT JOIN departamento d ON f.coddepartamento = d.codigo WHERE p.codigo = %s', [cod])
                linha = cur.fetchall()
                projeto = Projeto(linha[0][1], linha[0][2])
                projeto.cod = linha[0][0]
                if(linha[0][3] == None):
                    con.commit()
                    cur.close()
                else:
                    for l in linha:
                        daoF = FuncionarioDAO()
                        # print(l[3])
                        funcionario = daoF.buscar(l[3])
                        projeto.vinculaFuncionario(funcionario)
                        # print(projeto.funcionarios)
                    con.commit()
                    cur.close()
                return projeto
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.") 

    def salvar(self, projeto):
        try:
            with connect(self._con) as conn:
                dao = ProjetoDAO()
                cur = conn.cursor()
                if(projeto.cod == None):
                    dao.inserir(projeto)
                else:
                    dao.alterar(projeto)
                dao.vinculoFuncionario(projeto)
                conn.commit()
                cur.close()
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")

    def vinculoFuncionario(self, projeto):
        try:
            with connect(self._con) as conn:
                cur = conn.cursor()
                sql = cur.execute('SELECT codigofuncionario FROM funcproj WHERE "codigoprojeto"=%s', [projeto.cod])
                vetBD = []
                vetFunc = []
                for linha in cur.fetchall():
                    l = linha[0]
                    vetBD.append(l)
                for f in projeto.funcionarios:
                    if(not vetBD.__contains__(f.cod)):
                        sql = cur.execute('INSERT INTO funcproj (codigofuncionario, codigoprojeto) VALUES (%s, %s)',[f.cod, projeto.cod])
                    vetFunc.append(f.cod)
                for cod in vetBD:
                    if(not vetFunc.__contains__(cod)):
                        sql = cur.execute('DELETE FROM funcproj WHERE codigofuncionario = %s', [cod])
                conn.commit() 
                cur.close()
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")

    def listar(self):
        vet = []
        try:
            with connect(self._con) as con:
                cur = con.cursor()
                cur.execute("SELECT * FROM projeto")
                for linha in cur.fetchall():
                    proj = Projeto(linha[1], linha[2])
                    proj.cod = linha[0]
                    vet.append(proj)
                con.commit()
                cur.close()
                return vet
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")


if (__name__ == '__main__'):
    dao = ProjetoDAO()
    daoF = FuncionarioDAO()
    # projeto = Projeto("Testando", datetime())
    # projeto = Projeto("Ter a criatividade da thamyris pra inserir dados", datetime(2019, 5, 21))
    # dao.inserir(projeto)
    # print(projeto)
    # projeto = Projeto("Teste", datetime(2020, 3, 12))
    # func1 = daoF.buscar(9)
    # func2 = daoF.buscar(8)
    # func3 = daoF.buscar(12)
    # projeto = dao.buscar(6)
    # brenda = daoF.buscar(9)
    # celso = daoF.buscar(12)
    # # projeto.vinculaFuncionario(func1)
    # # projeto.vinculaFuncionario(func2)
    # # projeto.vinculaFuncionario(func3)
    # # dao.vinculaFuncionario(projeto)
    # projeto.desvinculaFuncionario(celso)
    # projeto.vinculaFuncionario(brenda)
    # dao.salvar(projeto)
    print(dao.listar())