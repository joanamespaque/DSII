from psycopg2 import connect
from bancodeseries.models.serie import Serie
from bancodeseries.models.usuario import Usuario
from bancodeseries.models.usuarioDAO import UsuarioDAO
from bancodeseries.models.dao import DAO

class SerieDAO(DAO):
    def excluir(self, serie):
        try:
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute('DELETE FROM serie WHERE cod=%s', [serie.cod])
                conn.commit()
                cur.close()
        except BaseException as e:
            print('problema ao excluir serie')
            raise e

    def inserir(self, serie):
        try:
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                if(hasattr(serie, "_foto")):
                    cur.execute('INSERT INTO serie (titulo, foto, codusuario) VALUES (%s, CURVAL(serie_cod_seq), %s) RETURNING cod', [serie.titulo, serie.usuario.cod])
                else:
                    cur.execute('INSERT INTO serie (titulo,codusuario) VALUES (%s, %s) RETURNING cod', [serie.titulo, serie.usuario.cod])
                row = cur.fetchone()
                serie.cod = row[0]
                conn.commit()
                cur.close()
        except BaseException as e:
            print("Problema ao inserir série.")
            raise e

    def listar(self, limit, offset):
        vet = []
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute('SELECT *FROM "serie" LIMIT %s OFFSET %s',[limit, offset])
                for row in cur.fetchall():
                    usuario = UsuarioDAO().buscar(Usuario(cod=row[3]))
                    vet.append(Serie(cod=row[0], titulo=row[1], foto=row[2], usuario=usuario))
                conn.commit()
                cur.close()
        except BaseException as e:
            print("Problema ao listar series.")
            raise e
        return vet

    def alterar(self, serie):
        try:
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                if(hasattr(serie, "_foto")):
                    cur.execute('UPDATE serie SET titulo=%s, foto=CURVAL(serie_cod_seq) WHERE cod = %s',[serie.titulo, serie.cod])
                else:
                    cur.execute('UPDATE serie SET titulo=%s WHERE cod = %s', [serie.titulo, serie.cod])

                conn.commit()
                cur.close()
        except BaseException as e:
            print('Problema ao alterar serie')
            raise e 

    def buscar(self, serie):
        try:
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute('SELECT s."cod", s."titulo", s."foto",\
                u."cod",u."nome", u."login", u.email, u.altura, u.validado, u.idade FROM "serie" s LEFT JOIN "usuario" u \
                ON u."cod" = s."codusuario" WHERE s."cod"=%s', [serie.cod])
                row = cur.fetchone()
                user = Usuario(cod=row[3], nome=row[4], login=row[5], email=row[6], altura=row[7], validado=row[8], idade=row[9])
                serie = Serie(cod=row[0], titulo=row[1], foto=row[2], usuario=user)
                conn.commit()
                cur.close()
                return serie
        except BaseException as e:
            print("problema ao buscar serie...")
            raise e
    
    def salvar(self, serie):
        if serie.persistido():
            self.alterar(serie)
        else:
            self.inserir(serie)
        
