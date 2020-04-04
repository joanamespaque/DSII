from .. import db
# from sqlalchemy.dialects.postgresql import CHAR 

class Autor(db.Model):
    __tablename__ = 'autor'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.CHAR(14), unique=True, nullable=False)

    def insere(self):
        db.session.add(self)
        db.session.commit()    

