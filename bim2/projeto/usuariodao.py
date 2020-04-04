from usuario import Usuario
from psycopg2 import connect
from dao import DAO

class UsuarioDao(DAO):
    def __init__(self):
        super().__init__()
    
    def buscar(self, usuario):
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
        #TODO: metododinho que busca um usuario com a senha e login passados por parâmetro através de usuario 