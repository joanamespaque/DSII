from .. import db 
from .. models.autor import Autor
autorlivro = db.Table('autorlivro', 
db.Column('idlivro',db.Integer, db.ForeignKey('livro.id', ondelete='cascade'), primary_key=True), 
db.Column('idautor', db.Integer, db.ForeignKey('autor.id', ondelete='cascade'), primary_key=True))

class Livro(db.Model):
    __tablename__ = 'livro'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    editora = db.Column(db.String(50), nullable=False)
    data_lancamento = db.Column(db.Date, nullable=False)
    autores = db.relationship('Autor',  secondary=autorlivro, backref=('livros'))

    def vinculaAutores(self, ids):
        self.autores.clear()
        for id in ids:
            a = Autor.query.get(id)
            self.autores.append(a)
        db.session.commit()

    def insert(self, ids):
        db.session.add(self)
        db.session.commit()
        self.vinculaAutores(ids)
    
    def excluir(self):
        db.session.delete(self)
        db.session.commit()        
