from flask import Flask, jsonify, Blueprint, request, render_template, redirect, url_for, session
from datetime import datetime
from .. models.usuario import Usuario
from .. models.pasta import Pasta
from .. models.pin import Pin
from flask_login import login_required, current_user
from .. import db
import json

pasta = Blueprint('pasta', __name__, url_prefix='/pasta')

@pasta.route('/inserir')
@login_required
def inserir():
    if(session['user_id']):
        return render_template('inserirpastas.html')
    else:
        redirect('/')

@pasta.route('/buscar', methods=['GET'])
def buscar():
    id = int(request.values['id'])
    pasta = Pasta.query.get(id)
    return jsonify(pasta = json.dumps(pasta.toDict()))

@pasta.route("/listar", methods=['GET'])
def listar():
    pastas = Pasta.query.all()
    lista = {}
    for p in pastas:
        lista.update({p.id : p.nome})
    return jsonify(pastas = json.dumps(lista)) 

@pasta.route('/cadastrar', methods=["GET", "POST"])
@login_required
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        try:
            secreto = request.form['secreto']
            secreto = True
        except: 
            secreto = False
        idcriador = session['user_id']
        pasta = Pasta(nome=nome, descricao=descricao, secreto=secreto, idcriador=idcriador, data_atualizacao = datetime.now())
        if(request.values.has_key('id')):
            pasta.id = request.form['id']
        pasta.salva()
        return redirect(url_for('usuario.listarpastas'))
    return render_template('index.html')

@pasta.route('/editar', methods=["GET"])
@login_required
def editar():
    id = request.values["id"]
    pasta = Pasta.query.filter_by(id=id).first()
    return render_template("updatepasta.html", p=pasta)

@pasta.route('/delete', methods=["GET"])
@login_required
def delete():
    id = int(request.values["id"])
    pasta = Pasta.query.get(id)
    pasta.excluir()
    return redirect(url_for('usuario.listarpastas'))
