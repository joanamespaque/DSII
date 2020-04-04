from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
from .app import db
from .app.controllers.livro import livro 
from .app.models.autor import Autor 
import os

app = Flask(__name__, template_folder='app/templates')
app.register_blueprint(livro)

uri = 'postgresql://postgres:postgres@localhost:5432/livrariads2'
app.config['SQLALCHEMY_DATABASE_URI'] = uri 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = 'alohomora'
app.debug = True 
db.init_app(app)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/create')
def create():
    db.create_all()
    return 'tabelinhas criadas'

@app.route('/drop')
def drop():
    db.drop_all()
    return 'tabelinhas deletadas'

@app.route('/popula_autores')
def popula_autores():
    autor1 = Autor(nome='BauhausCyr Scliar', cpf = '00011122200')
    autor2 = Autor(nome='Cerrote de Assis', cpf = '33322211100')
    autor3 = Autor(nome='J. K. Rowling in the Deep', cpf = '99988877700')
    autor1.insere()
    autor2.insere()
    autor3.insere()
    return 'autores criados'
