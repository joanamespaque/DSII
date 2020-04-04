from dao import DAO 
import psycopg2
from psycopg2 import connect
from filme import Filme
class FilmeDAO(DAO):
    def __init__(self):
        super().__init__()

    def listar(self, limit, offset):
        vet = []
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute('SELECT "id", "titulo", "direcao", "genero"\
                FROM "filme" ORDER BY id ASC LIMIT %s OFFSET %s',[limit, offset])
                for row in cur.fetchall():
                    vet.append(Filme(id=row[0], titulo=row[1],direcao = row[2], genero = row[3]))
                cur.close()
        except BaseException as e:
            print ("Problema ao listar")
            raise e    
        return vet

    def buscar(self, id):
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute('SELECT "id", "titulo", "direcao", "genero", "duracao", "sinopse", "elenco", "dataLancamento", "classificacao"\
                FROM "filme" WHERE id=%s',[id])
                row = cur.fetchone()
                filme = Filme(id=row[0], titulo=row[1], direcao = row[2], genero = row[3], duracao = row[4], sinopse = row[5], elenco = row[6], dataLancamento = row[7], classificacao = row[8])
                cur.close()
        except BaseException as e:
            print ("Problema ao listar")
            raise e    
        return filme

# if __name__ == "__main__":
#     dao = FilmeDAO()
#     # print(dao.listar(10,0))
#     print(dao.buscar(1))