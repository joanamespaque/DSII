from psycopg2 import connect
from bancodeseries.models.temporada import Temporada
from bancodeseries.models.serie import Serie
from bancodeseries.models.serieDAO import SerieDAO
from bancodeseries.models.dao import DAO

class TemporadaDAO(DAO):
    def inserir(self, temporada):
        try:
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO temporada (numero, titulo, codserie) VALUES ((SELECT coalesce(MAX(numero),0)+1 FROM temporada WHERE codserie = %s), %s, %s) RETURNING cod", [temporada.serie.cod, temporada.titulo, temporada.serie.cod])
                row = cur.fetchone()
                temporada.cod = row[0]
                conn.commit()
                cur.close()
        except BaseException as e:
            print("erro ao inserir temporada")
            raise e
    
    def excluir(self, temporada):
        try:
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute("DELETE FROM temporada WHERE cod = %s", [temporada.cod])
                conn.commit()
                cur.close()
        except BaseException as e:
            print("erro ao excluir temporada")
            raise e

    def alterar(self, temporada):
        try:
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute("UPDATE temporada SET titulo = %s, WHERE cod = %s", [temporada.titulo, temporada.cod])
                conn.commit()
                cur.close()
        except BaseException as e:
            print("erro ao alterar temporada")
            raise e
    
    def listar(self, serie, limit, offset):
        vet = []
        try:
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM temporada WHERE codserie=%s LIMIT %s OFFSET %s",[serie.cod, limit, offset])
                for row in cur.fetchall():
                    vet.append(Temporada(cod = row[0], titulo=row[1], numero=row[2], serie=serie))
                conn.commit()
                cur.close()
        except BaseException as e:
            print("Problema ao listar temporadas.")
            raise e
        return vet

    def buscar(self, temporada):
        try:
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM temporada WHERE cod = %s", [temporada.cod])
                row = cur.fetchone()
                serie = SerieDAO().buscar(Serie(cod=row[3]))
                temporada = Temporada(cod=row[0], titulo=row[1], numero=row[2], serie=serie)
                conn.commit()
                cur.close()
                return temporada 
        except BaseException as e:
            print("erro ao buscar temporada")
            raise e

    def salvar(self, temporada):
        if temporada.persistido():
            self.alterar(temporada)
        else:
            self.inserir(temporada)
        




