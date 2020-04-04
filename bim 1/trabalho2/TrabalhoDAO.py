from AutorDAO import *
from Trabalho import Trabalho
from datetime import datetime
class TrabalhoDAO(DAO):
    def __init__(self):
        super().__init__()
    # def entregaTrabalho()
    def inserir(self, trabalho):
        try:
            with connect(self._con) as conn:
                cur = conn.cursor()
                sql = cur.execute('INSERT INTO "Trabalho" (conteudo, nota, titulo, "dataHoraAtualizacao") VALUES (%s, %s, %s, now()) returning cod', [trabalho.conteudo, trabalho.nota, trabalho.titulo])
                linha = cur.fetchone()
                trabalho.cod = linha[0]
                conn.commit()
                cur.close()
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")
    def alterar(self, trabalho):
        try:
            with connect(self._con) as conn:
                cur = conn.cursor()
                sql = cur.execute('UPDATE "Trabalho" SET conteudo=%s, nota =%s, titulo=%s, "dataHoraAtualizacao"=now(), "dataEntrega" = %s WHERE cod = %s and "dataHoraAtualizacao" = %s', [trabalho.conteudo, trabalho.nota, trabalho.titulo, trabalho.dataEntrega ,trabalho.cod, trabalho.dataHoraAtualizacao]) 
                conn.commit()
                cur.close()
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")
    def vinculaAutor(self, trabalho):
        try:
            with connect(self._con) as conn:
                cur = conn.cursor()
                sql = cur.execute('SELECT "codAutor" FROM "TrabalhoAutor" WHERE "codTrabalho"=%s', [trabalho.cod])
                vet = []
                for linha in cur.fetchall():
                    l = linha[0]
                    vet.append(l)
                for a in trabalho.autores:
                    if(not vet.__contains__(a.cod)):
                        sql = cur.execute('INSERT INTO "TrabalhoAutor" ("codAutor", "codTrabalho") VALUES (%s, %s)',[a.cod, trabalho.cod] )
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")
    def salvar(self, trabalho):
        try:
            with connect(self._con) as conn:
                dao = TrabalhoDAO()
                cur = conn.cursor()
                if(trabalho.cod == None):
                    dao.inserir(trabalho)
                else:
                    dao.alterar(trabalho)
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")

    def excluir(self, cod):
        try:
            with connect(self._con) as conn:
                cur = conn.cursor()
                sql = cur.execute('DELETE FROM "Trabalho" WHERE cod=%s', [cod])
                conn.commit() 
                cur.close()
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")
    def buscar(self, cod): 
        try:
            with connect(self._con) as con:
                cur = con.cursor()
                cur.execute('SELECT t.cod, t.conteudo, t.nota, t.titulo, t."dataEntrega",t."dataHoraAtualizacao",a.nome, a.email FROM "Trabalho" t LEFT JOIN "TrabalhoAutor" ta ON  t.cod = ta."codTrabalho" LEFT JOIN "Autor" a ON a.cod = ta."codAutor" WHERE t.cod = %s', [cod])
                linha = cur.fetchall()
                trabalho = Trabalho(linha[0][3], linha[0][1], linha[0][2])
                trabalho.dataEntrega = linha[0][4]
                trabalho.dataHoraAtualizacao = linha[0][5]
                trabalho.cod = linha[0][0]
                if(linha[0][7] == None):
                    con.commit()
                    cur.close()
                else:
                    for l in linha:
                        autor = Autor(l[6], l[7])
                        trabalho.vinculaAutor(autor)
                    con.commit()
                    cur.close()
                return trabalho
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")
    def listar(self):
        vet = []
        try:
            with connect(self._con) as con:
                cur = con.cursor()
                cur.execute('SELECT * FROM "Trabalho"')
                for linha in cur.fetchall():
                    trabalho = Trabalho(linha[4], linha[1], linha[2])
                    trabalho.cod = linha[0]
                    trabalho.dataEntrega = linha[3]
                    trabalho.dataHoraAtualizacao = linha[5]
                    vet.append(trabalho)
                cur.close()
                return vet
        except psycopg2.OperationalError:
            print("Erro ao estabelecer conexão.")    
