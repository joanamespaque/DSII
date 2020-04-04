from .. import db 

class Pin(db.Model):
    __tablename__ = 'pin'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    descricao = db.Column(db.String(350), nullable=False)
    data_atualizacao = db.Column(db.DateTime, nullable=False)
    imagem = db.Column(db.String(100))
    tematica = db.Column(db.String(100), nullable=False)
    idcriador = db.Column(db.Integer, db.ForeignKey('usuario.id', ondelete='set null', onupdate='cascade'))
    criador = db.relationship('Usuario', lazy= 'joined', uselist= False, cascade="save-update, merge")
    idpastaorigem = db.Column(db.Integer, db.ForeignKey('pasta.id', ondelete='set null', onupdate='cascade'))
    pastaorigem = db.relationship('Pasta', lazy= 'joined', uselist= False, cascade="save-update, merge")

    def salva(self):
        if(self.id):
            self = db.session.merge(self)
        else:
            db.session.add(self)
        db.session.commit()
        # return self
    
    def excluir(self):
        db.session.delete(self)
        db.session.commit()
    
    def toDict(self):
        dict = {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "imagem": self.imagem,
            "tematica": self.tematica,
            "idcriador": self.idcriador
        }
        return dict 