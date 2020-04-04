from FuncionarioDAO import *
from Projeto import Projeto 
from datetime import datetime
class ProjetoDAO:
    def __init__(self):
        self._con = 'dbname=aula1 user=postgres password=postgres host=localhost port=5432'
    def inserir(self, projeto):
        try:
            with connect(self._con) as conn:
                cur = conn.cursor()
                sql = cur.execute('INSERT INTO projeto (nome, data) VALUES (%s, %s)', [projeto.nome, projeto.data])
                # print(cur.query)
                conn.commit()
                cur.close()
        except Exception as e:
            print("treta")
            raise e
# if (__name__ == '__main__'):
#     dao = ProjetoDAO()
#     projeto = Projeto("Testando", datetime())
