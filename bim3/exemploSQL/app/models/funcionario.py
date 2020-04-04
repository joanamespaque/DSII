from .. import db 
# from . departamento import Departamento

class Funcionario(db.Model):
    __tablename__ = 'funcionario'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    iddepto = db.Column(db.Integer, db.ForeignKey('departamento.id', ondelete='cascade', onupdate='cascade'))
    def salva(self):
        if(self.id):
            self = db.session.merge(self)
        else:
            db.session.add(self)
        db.session.commit()
    
    def excluir(self):
        db.session.delete(self)
        db.session.commit()        
