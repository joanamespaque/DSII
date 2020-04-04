from .. import db 
from . endereco import Endereco
from . funcionario import Funcionario
class Departamento(db.Model):
    __tablename__ = 'departamento'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    data_atualizacao = db.Column(db.DateTime, unique=True, default=db.func.now(), onupdate=db.func.now())
    funcionarios = db.relationship ('Funcionario', backref= 'departamento', lazy= 'select')
    endereco = db.relationship('Endereco', lazy= 'joined', uselist= False, cascade="save-update, merge, delete")
    idendereco = db.Column(db.Integer, db.ForeignKey('endereco.id', ondelete='set null', onupdate='cascade'))

    # delete-orphan

    def salva(self):
        if(self.id):
            self = db.session.merge(self)
        else:
            db.session.add(self)
        db.session.commit()
    
    def excluir(self):
        db.session.delete(self)
        db.session.commit()        
