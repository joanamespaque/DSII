from .. import db 
from .. models.pasta import Pasta
from flask_login import UserMixin
segue_usuario = db.Table('segueUsuario', 
db.Column('idseguido', db.Integer, db.ForeignKey('usuario.id', ondelete='cascade')),
db.Column('idseguidor', db.Integer, db.ForeignKey('usuario.id', ondelete='cascade')),  extend_existing=True)

segue_pasta = db.Table('seguePasta', 
db.Column('idseguidor', db.Integer, db.ForeignKey('usuario.id', ondelete='cascade'), primary_key=True), 
db.Column('idpasta', db.Integer, db.ForeignKey('pasta.id', ondelete='cascade'), primary_key=True), extend_existing=True)

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    foto = db.Column(db.String(200))
    validado = db.Column(db.Boolean, nullable=False)
    seguidores = db.relationship('Usuario',  secondary=segue_usuario, primaryjoin=(segue_usuario.c.idseguidor) == id, secondaryjoin=(segue_usuario.c.idseguido==id), backref=('seguidos'), lazy='dynamic')
    pastasSeguidas = db.relationship('Pasta', secondary=segue_pasta, backref=('seguidores')) 

    def salvar(self):
        if(self.id):
            self = db.session.merge(self)
        else:
            db.session.add(self)
        db.session.commit()
    
    def excluir(self):
        db.session.delete(self)
        db.session.commit()        

    def validaUsuario(self):
        self.validado = True
        db.session.commit()
        
    def verificaLogin(self):
        result = Usuario.query.filter_by(email=self.email).first()
        if(result):
            return True
        else:
            return False
    
    def __srt__(self):
        return self.nome
    
    def toDict(self):
        dict = {
            "id": self.id,
            "nome": self.nome,
            "username": self.username,
            "foto": self.foto,
            "email": self.email
        }
        return dict   