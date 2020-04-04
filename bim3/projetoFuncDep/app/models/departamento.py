from .. import db 

class Departamento(db.Model):
    __tablename__ = 'departamento'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    data_atualizacao = db.Column(db.DateTime, unique=True, default=db.func.now(), onupdate=db.func.now())

    def salva(self):
        db.session.add(self)
        db.session.commit()
    
    def excluir(self):
        db.session.delete(self)
        db.session.commit()        
