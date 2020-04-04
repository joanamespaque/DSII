from .. import db 

class Endereco(db.Model):
    __tablename__ = 'endereco'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False)
    rua = db.Column(db.String(100), nullable=False)

    def salva(self):
        if(self.id):
            self = db.session.merge(self)
        else:
            db.session.add(self)
        db.session.commit()
        
    def excluir(self):
        db.session.delete(self)
        db.session.commit()        
