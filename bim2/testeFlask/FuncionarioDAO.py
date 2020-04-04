import psycopg2
from psycopg2 import connect
from Funcionario import *
from DepartamentoDAO import *
class FuncionarioDAO:
    def __init__(self):
        self._con = 'dbname=aula1 user=postgres password=postgres host=localhost port=5432'
    def inserir(self, funcionario):
        try:
            with connect(self._con) as conn:
                cur = conn.cursor()
                sql = cur.execute('INSERT INTO funcionario (nome, coddepartamento, login, senha, adm) VALUES (%s, %s, %s, %s, %s) returning codigo', [funcionario.nome, funcionario.departamento.cod, funcionario.login, funcionario.senha, funcionario.adm])
                linha = cur.fetchone()
                funcionario.cod = linha[0]
                # print(cur.query)
                conn.commit()
                cur.close()
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")

    def excluir(self, cod):
        try:
            with connect(self._con) as conn:
                cur = conn.cursor()
                sql = cur.execute("DELETE FROM funcionario WHERE codigo=%s", [cod])
                conn.commit() 
                cur.close()
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")

    def listar(self):
        vet = []
        try:
            with connect(self._con) as com:
                cur = com.cursor()
                cur.execute("SELECT codigo, nome, login, adm FROM funcionario")
                for linha in cur.fetchall():
                    func = Funcionario(linha[1], linha[2], linha[3])
                    func.cod = linha[0]
                    vet.append(func)
                cur.close()
                return vet
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")

    def salvar(self, funcionario):
        dao = FuncionarioDAO()
        if(funcionario.cod==None):
            dao.inserir(funcionario)
        else:
            dao.alterar(funcionario)
    
    def buscarLogin(self, login, senha):
        try:
            with connect(self._con) as conn:
                cur = conn.cursor()
                cur.execute("SELECT codigo, nome, login, senha, adm FROM funcionario WHERE login = %s and senha =%s", [login, senha])
                linha = cur.fetchone()
                if(linha!=None):
                    funcionario = Funcionario(linha[1], linha[2], linha[3], linha[4])
                    funcionario.cod = linha[0]
                else:
                    funcionario = False
            
                conn.commit()
                cur.close()
                # return linha
                return funcionario
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")
    
    def buscar(self, cod):
        try:
            with connect(self._con) as conn:
                cur = conn.cursor()
                cur.execute("SELECT f.codigo, f.nome, f.login, f.senha, f.adm, f.coddepartamento, d.nome, d.dt_atu FROM funcionario f INNER JOIN departamento d ON f.coddepartamento = d.codigo WHERE f.codigo = %s", [cod])
                # cur.execute("SELECT codigo, nome, dt_atu FROM departamento WHERE codigo=%s", str(cod))
                linha = cur.fetchall()
                funcionario = Funcionario(linha[0][1], linha[0][2], linha[0][3])
                funcionario.cod = linha[0][0]
                funcionario.adm = linha[0][4]
                departamento = Departamento(linha[0][6])
                departamento.cod = linha[0][5]
                departamento.dt_atu = linha[0][7]
                funcionario.departamento = departamento
                conn.commit()
                cur.close()
                return funcionario
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")

    def alterar(self, funcionario):
        try: 
            with connect(self._con) as conn:
                cur = conn.cursor()
                sql = cur.execute("UPDATE funcionario SET nome = %s, coddepartamento = %s, login = %s, senha=%s, adm=%s WHERE codigo = %s",[funcionario.nome, funcionario.departamento.cod, funcionario.login, funcionario.senha, funcionario.adm, funcionario.cod])
                conn.commit()
                cur.close
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")

    def listaProjetos(self, funcionario):
        vet = []
        try: 
            with connect(self._con) as conn:
                cur = conn.cursor()
                sql = cur.execute('SELECT p.codigo, p.nome, p.data FROM projeto p INNER JOIN funcproj fp ON p.codigo = fp."codigoProjeto" WHERE fp."codigoFuncionario" = %s', [funcionario.cod])
                # print(cur.fetchall())
                for linha in cur.fetchall():
                    proj = Projeto(linha[1], linha[2])
                    proj.cod = linha[0]
                    vet.append(proj) 
                conn.commit()
                cur.close()
                return vet
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")
	
        
# if (__name__ == '__main__'):
    # daoD = DepartamentoDAO()
    # daoF = FuncionarioDAO()
    # # dep = Departamento("mudaTESTE")
    # # dep.cod = 5
    # # dep1 = Departamento("teste")
    # # dep1 = Departamento("alo celso")
    # # dao.inserir(dep1)
    # # dao.excluir(7)
    # # depto1 = daoD.buscar(1)
    # # funcionario = Funcionario("Pipipipopopo")
    # # funcionario.departamento = depto1
    # # funcionario.cod = 4
    # func = daoF.buscar(2)
    # print(daoF.listaProjetos(func))
    # print(daoF.listar())
    


    # print(dao.listar())
    # dao.alterar(dep)
    