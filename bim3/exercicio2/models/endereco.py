from flask import Flask,render_template, request,session, redirect
from flask_sqlalchemy import SQLAlchemy


from departamento import Departamento

app = Flask(__name__)


uri= 'postgresql://postgres:postgres@localhost:5432/exercicio'
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.init_app(app)

class Endereco(db.Model):
    __tablename__ = 'endereco'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False)
    rua = db.Column(db.String(100), nullable=False)

    def salvar(self, e):
        #verifica=hasattr(d, 'id')
        if (e.id):
            db.session.merge(e)
            db.session.commit()
        else:
            print(e.id)
            print("endereco: nao tem id")
            db.session.add(e)
            db.session.commit()
 
    def excluir(self,id):
        db.session.delete(id)
        db.session.commit()
    

