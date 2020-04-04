from flask import Flask, Blueprint, session, request, redirect, render_template, url_for
from .pintarest import db, app
from .pintarest.controllers.usuario import usuario
from .pintarest.models.usuario import Usuario
from .pintarest.controllers.pasta import pasta
from .pintarest.controllers.pin import pin
from .pintarest.models.pin import Pin
from hashlib import md5 
import os

app.register_blueprint(usuario)
app.register_blueprint(pasta)
app.register_blueprint(pin)

uri = 'postgresql://postgres:postgres@localhost:5432/pintarest'
app.config['SQLALCHEMY_DATABASE_URI'] = uri 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = 'alohomora'
app.debug = True 
app.config.update(dict(
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SQLALCHEMY_DATABASE_URI = uri,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_USERNAME='exerciciotesteds2@gmail.com',
    MAIL_DEFAULT_SENDER='exerciciotesteds2@gmail.com',
    MAIL_PASSWORD='vishmarinamail',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USE_TLS=False,
    UPLOAD_FOLDER='uploads',
    TEMPLATE_FOLDER='templates',
    STATIC_FOLDER='static',
    TESTING=False
))
db.init_app(app)

@app.route('/')
def index():
    pin_query = Pin.query.all()
    return render_template('index.html', pins = pin_query)

@app.before_first_request
def criatabelas():
    db.create_all()

@app.route('/create_users')
def create():
    user1 = Usuario(nome="Joana Mespaque", email="joanamespaque@gmail.com", senha=md5("joanamespaque".encode('utf-8')).hexdigest(), username="joanamespaque", foto="profile.png", validado=True)
    user2 = Usuario(nome="Davi Ferreira", email="daviferreira@gmail.com", senha=md5("daviferreira".encode('utf-8')).hexdigest(), username="daviferreira", foto="profile.png", validado=True)
    user1.salvar()
    user2.salvar()
    return redirect('/')

@app.route('/drop')
def drop():
    db.drop_all()
    return 'tabelinhas deletadas'