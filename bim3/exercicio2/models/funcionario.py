
from flask import Flask,render_template, request,session, redirect
from flask_sqlalchemy import SQLAlchemy
from departamento import Departamento

app = Flask(__name__)


uri= 'postgresql://postgres:postgres@localhost:5432/exercicio'
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.init_app(app)

class Funcionario(db.Model):
    __tablename__ = 'funcionario'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    iddepartamento = db.Column(db.Integer, db.ForeignKey('departamento.id', ondelete='cascade', onupdate='cascade'))





