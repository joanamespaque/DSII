from flask import Flask,render_template, request,session, redirect
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

from controllers.departamento import *

#from controllers.funcionario import Funcionario
#from controllers.endereco import Endereco
#from models.endereco import Endereco
#from models.funcionario import Funcionario
#from models.departamento import Departamento


app = Flask(__name__)


uri= 'postgresql://postgres:postgres@localhost:5432/exercicio'
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.init_app(app)
#db = SQLAlchemy(app)
#db.init_app(app)


@app.before_first_request
def before():
    db.create_all()



if __name__ == '__main__':
    app.secret_key = 'minha chave'
    app.env = 'development'
    app.run(debug = True)
