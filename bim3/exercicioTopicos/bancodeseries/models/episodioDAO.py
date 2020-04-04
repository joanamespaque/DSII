from psycopg2 import connect
from bancodeseries.models.episodio import Episodio
from bancodeseries.models.temporada import Temporada
from bancodeseries.models.temporadaDAO import TemporadaDAO
from bancodeseries.models.serie import Serie
from bancodeseries.models.serieDAO import SerieDAO
from bancodeseries.models.dao import DAO

class EpisodioDAO(DAO):
    def inserir(self, episodio):
        try:
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO episodio (numero, titulo, codserie, codtemporada) VALUES ((SELECT coalesce(MAX(numero),0)+1 FROM episodio WHERE codserie = %s and codtemporada =%s), %s, %s, %s) RETURNING cod", [episodio.temporada.serie.cod, episodio.temporada.cod, episodio.titulo, episodio.temporada.serie.cod, episodio.temporada.cod])
                row = cur.fetchone()
                episodio.cod = row[0]
                conn.commit()
                cur.close()
        except BaseException as e:
            print("erro ao inserir episodio")
            raise e
    
    def excluir(self, episodio):
        try:
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute("DELETE FROM episodio WHERE cod = %s", [episodio.cod])
                conn.commit()
                cur.close()
        except BaseException as e:
            print("erro ao excluir episodio")
            raise e

    def alterar(self, episodio):
        try:
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute("UPDATE episodio SET titulo = %s, WHERE cod = %s", [episodio.titulo, episodio.cod])
                conn.commit()
                cur.close()
        except BaseException as e:
            print("erro ao alterar episodio")
            raise e
    
    def listar(self, temporada, limit, offset):
        vet = []
        try:
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM episodio WHERE codserie=%s and codtemporada=%s LIMIT %s OFFSET %s",[temporada.serie.cod, temporada.cod, limit, offset])
                for row in cur.fetchall():
                    serie = SerieDAO().buscar(Serie(cod=temporada.serie.cod))
                    temporada = TemporadaDAO().buscar(Temporada(cod=temporada.cod))
                    vet.append(Episodio(cod = row[0], titulo=row[1], numero=row[3], serie=serie, temporada=temporada))
                conn.commit()
                cur.close()
        except BaseException as e:
            print("Problema ao listar episodios.")
            raise e
        return vet

    def buscar(self, episodio):
        try:
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM episodio WHERE cod = %s", [episodio.cod])
                row = cur.fetchone()
                serie = SerieDAO().buscar(Serie(cod=row[2]))
                temporada = TemporadaDAO().buscar(Temporada(cod=row[4]))
                episodio = Episodio(cod=row[0], titulo=row[1], numero=row[3], serie=serie, temporada=temporada)
                conn.commit()
                cur.close()
                return episodio
        except BaseException as e:
                print("erro ao buscar episodio")
                raise e
    
    def salvar(self, episodio):
        if episodio.persistido():
            self.alterar(episodio)
        else:
            self.inserir(episodio)
        





