from DAO import *
from Autor import Autor 
class AutorDAO(DAO):
    def __init__(self):
        super().__init__()
    def inserir(self, autor):
        try:
            with connect(self._con) as conn:
                cur = conn.cursor()
                sql = cur.execute('INSERT INTO "Autor" (nome, email) VALUES (%s, %s)  returning cod', [autor.nome, autor.email])
                linha = cur.fetchone()
                autor.cod = linha[0]
                conn.commit()
                cur.close()
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")
    def alterar(self, autor):
        try:
            with connect(self._con) as conn:
                cur = conn.cursor()
                sql = cur.execute('UPDATE "Autor" SET nome = %s, email = %s WHERE cod = %s', [autor.nome, autor.email, autor.cod])
                conn.commit()
                cur.close()
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")
            
    def salvar(self, autor):
        dao = AutorDAO()
        if(autor.cod==None):
            dao.inserir(autor)
        else:
            dao.alterar(autor)

    def excluir(self, cod):
        try:
            with connect(self._con) as conn:
                cur = conn.cursor()
                sql = cur.execute('DELETE FROM "Autor" WHERE cod=%s', [cod])
                conn.commit() 
                cur.close()
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")
    def listar(self):
        vet = []
        try:
            with connect(self._con) as con:
                cur = con.cursor()
                cur.execute('SELECT * FROM "Autor"')
                for linha in cur.fetchall():
                    autor = Autor(linha[1], linha[2])
                    autor.cod = linha[0]
                    vet.append(autor)
                con.commit()
                cur.close()
                return vet
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")
    def buscar(self, cod): 
        try:
            with connect(self._con) as con:
                cur = con.cursor()
                cur.execute('SELECT cod, nome, email FROM "Autor" WHERE cod = %s', [cod])
                linha = cur.fetchone()
                autor = Autor(linha[1], linha[2])
                autor.cod = linha[0]
                con.commit()
                cur.close()
                return autor 
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")                
    # def listaTrabalhos()
