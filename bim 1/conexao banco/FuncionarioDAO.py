from DepartamentoDAO import *
from Funcionario import Funcionario 
from Projeto import Projeto
class FuncionarioDAO:
    def __init__(self):
        self._con = 'dbname=aula1 user=postgres password=postgres host=localhost port=5432'
    def inserir(self, funcionario):
        try:
            with connect(self._con) as conn:
                cur = conn.cursor()
                sql = cur.execute('INSERT INTO funcionario (nome, coddepartamento) VALUES (%s, %s)', [funcionario.nome, funcionario.departamento.cod])
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
                sql = cur.execute("DELETE FROM funcionario WHERE codigo=%s", str(cod))
                conn.commit() 
                cur.close()
        except Exception as e:
            print("Treta")
            raise e 

    def listar(self):
        vet = []
        try:
            with connect(self._con) as com:
                cur = com.cursor()
                cur.execute("SELECT codigo, nome FROM funcionario")
                for linha in cur.fetchall():
                    func = Funcionario(linha[1])
                    func.cod = linha[0]
                    vet.append(func)
                cur.close()
                return vet
        except BaseException as e: 
            print("treta")
            raise e
    
    def buscar(self, cod):
        try:
            with connect(self._con) as conn:
                cur = conn.cursor()
                cur.execute("SELECT f.codigo, f.nome, f.coddepartamento, d.nome, d.dt_atu FROM funcionario f INNER JOIN departamento d ON f.coddepartamento = d.codigo WHERE f.codigo = %s", [cod])
                # cur.execute("SELECT codigo, nome, dt_atu FROM departamento WHERE codigo=%s", str(cod))
                linha = cur.fetchall()
                funcionario = Funcionario(linha[0][1])
                funcionario.cod = linha[0][0]
                departamento = Departamento(linha[0][3])
                departamento.cod = linha[0][2]
                departamento.dt_atu = linha[0][4]
                funcionario.departamento = departamento
                conn.commit()
                cur.close()
                return funcionario
        except Exception as e:
            print("Treta")
            raise e
    def alterar(self, funcionario):
        try: 
            with connect(self._con) as conn:
                cur = conn.cursor()
                sql = cur.execute("UPDATE funcionario SET nome = %s, coddepartamento = %s WHERE codigo = %s",[funcionario.nome, funcionario.departamento.cod, funcionario.cod])
                conn.commit()
                cur.close
        except Exception as e:
            print("TRETA")
            raise e
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
        except Exception as e:
            print("TRETA")
            raise e
	
        
if (__name__ == '__main__'):
    daoD = DepartamentoDAO()
    daoF = FuncionarioDAO()
    # dep = Departamento("mudaTESTE")
    # dep.cod = 5
    # dep1 = Departamento("teste")
    # dep1 = Departamento("alo celso")
    # dao.inserir(dep1)
    # dao.excluir(7)
    # depto1 = daoD.buscar(1)
    # funcionario = Funcionario("Pipipipopopo")
    # funcionario.departamento = depto1
    # funcionario.cod = 4
    func = daoF.buscar(2)
    print(daoF.listaProjetos(func))
    # print(daoF.listar())
    


    # print(dao.listar())
    # dao.alterar(dep)
    