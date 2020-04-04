from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .app import db
from .app.controllers.departamento import depto
from .app.controllers.funcionario import func
from .app.controllers.endereco import endereco
from .app.controllers.projeto import projeto
import os

app = Flask(__name__, template_folder='app/templates')
app.register_blueprint(depto)
app.register_blueprint(func)
app.register_blueprint(endereco)
app.register_blueprint(projeto)

uri = 'postgresql://postgres:postgres@localhost:5432/testebd'
app.config['SQLALCHEMY_DATABASE_URI'] = uri 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = 'alohomora'
app.debug = True 
db.init_app(app)

@app.before_first_request
def before_first_request():
    db.create_all()

@app.route('/drop_bd')
def drob_bd():
    db.drop_all()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.env = 'development'
    app.run('localhost', port = port)
    #  export FLASK_APP=run.py
    #  export FLASK_DEBUG=True
    #  export FLASK_ENV=development
