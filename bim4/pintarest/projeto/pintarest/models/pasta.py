from .. import db 
from .. models.pin import Pin

pasta_pin = db.Table('pastapin', 
db.Column('idpasta', db.Integer, db.ForeignKey('pasta.id', ondelete='cascade'), primary_key=True), 
db.Column('idpin', db.Integer, db.ForeignKey('pin.id', ondelete='cascade'), primary_key=True))

class Pasta(db.Model):
    __tablename__ = 'pasta'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    secreto = db.Column(db.Boolean, nullable=False)
    descricao = db.Column(db.String(500), nullable=False)
    data_atualizacao = db.Column(db.DateTime, nullable=False)
    idcriador = db.Column(db.Integer, db.ForeignKey('usuario.id', ondelete='set null', onupdate='cascade'))
    criador = db.relationship('Usuario', lazy= 'joined', uselist= False, cascade="save-update, merge")
    pins = db.relationship('Pin', backref='pastas', secondary=pasta_pin)

    def salva(self):
        if(self.id):
            self = db.session.merge(self)
        else:
            db.session.add(self)
        db.session.commit()
    
    def excluir(self):
        db.session.delete(self)
        db.session.commit()  

    
    def toDict(self):
        dict = {
            "id": self.id,
            "nome": self.nome,
            "secreto": self.secreto,
            "descricao": self.descricao,
            "idcriador": self.idcriador
        }
        return dict   
    