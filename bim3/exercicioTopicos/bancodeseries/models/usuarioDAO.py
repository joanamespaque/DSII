from psycopg2 import connect
from bancodeseries.models.usuario import Usuario
from bancodeseries.models.dao import DAO
class UsuarioDAO(DAO):
    def __init__(self):
        super().__init__()

    def buscar(self, usuario):
        try:
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute('SELECT * FROM usuario WHERE cod=%s', [usuario.cod])
                row = cur.fetchone()
                usu = Usuario(cod=row[0], nome=row[1], email=row[2], login=row[3], senha=row[4], altura=row[5], idade=row[6], validado=row[7])
                conn.commit()
                cur.close()
                return usu
        except BaseException as e:
            print ("Problema no buscar Usuario -- exception seguindo para ser tratada")
            raise e

    def login(self, usuario):
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute("SELECT cod, nome, login, senha from usuario where login = %s and senha = %s", [usuario.login, usuario.senha])
                row = cur.fetchone()
                if(row!=None):
                    u = Usuario(cod=row[0], nome=row[1], login=row[2])
                    u.cod = row[0]
                else:
                    u = False
                conn.commit()
                cur.close()
                return u
        except BaseException as e:
            print ("Problema no buscar -- exception seguindo para ser tratada")
            raise e    
    
    def excluir(self, usuario):
        try:
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute("DELETE FROM usuario WHERE cod=%s",[usuario.cod])
                conn.commit()
                # usuario.cod=None
                cur.close()
        except BaseException as e:
            print("Problema no excluir usuario -- exception seguindo para ser tratada")
            raise e

    def validaUsuario(self, cod):
        try:
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute('UPDATE usuario SET validado=true WHERE cod=%s',[cod])
                conn.commit()
                cur.close()
        except BaseException as e:
            print("Problema no excluir usuario -- exception seguindo para ser tratada")
            raise e
    
    def inserir(self, usuario):
        params = [usuario.nome,usuario.login, usuario.email, usuario.senha, usuario.altura, usuario.idade, usuario.validado]
        try:
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO usuario (nome, login, email, senha, altura, idade, validado) values (%s, %s, %s, %s, %s, %s, %s) RETURNING cod", params)
                row = cur.fetchone()
                usuario.cod = row[0]
                conn.commit()
                cur.close()
        except BaseException as e:
            print("Problema no inserir usuario -- exception seguindo para ser tratada")
            raise e
            
