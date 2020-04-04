
from flask import Flask,render_template, request,session, redirect
from flask_sqlalchemy import SQLAlchemy
#from controllers.endereco import Endereco
#from controllers.funcionario import Funcionario

#from endereco import Endereco
#from funcionario import Funcionario

app = Flask(__name__)


uri= 'postgresql://postgres:postgres@localhost:5432/exercicio'
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.init_app(app)


class Departamento(db.Model):
    __tablename__ = 'departamento'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data_atualizacao = db.Column(db.DateTime, unique=True,default=db.func.now(), onupdate=db.func.now())
    funcionarios = db.relationship ('Funcionario', backref= 'departamento', lazy= 'select')
    endereco = db.relationship ('Endereco', lazy= 'joined', uselist= False)
    idendereco = db.Column(db.Integer, db.ForeignKey('endereco.id', ondelete='set null', onupdate='cascade'))

    def salvar(self, d):
        #verifica=hasattr(d, 'id')
        if (d.id):
            db.session.merge(d)
            db.session.commit()
        else:
            print(d.id)
            print("dpto: nao tem id")
            db.session.add(d)
            db.session.commit()
 
    def excluir(self,id):
        db.session.delete(id)
        db.session.commit()






