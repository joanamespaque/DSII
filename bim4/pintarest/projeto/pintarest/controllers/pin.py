from flask import Flask, jsonify, Blueprint, request, render_template, redirect, url_for, session
from werkzeug.utils import secure_filename
from datetime import datetime
from flask_login import login_required, current_user
from .. models.usuario import Usuario
from .. models.pasta import Pasta
from .. models.pin import Pin
from .. import db
import json, os
import time
from ...pintarest import app
from sqlalchemy import text

pin = Blueprint('pin', __name__, url_prefix='/pin')
options = {
        'animais':'Animais e bichos de estimação',
        'arquitetura':'Arquitetura',
        'arte':'Arte',
        'artesanato':'Artesanato e faça você mesmo',
        'beleza':'Cabelo, maquiagem e beleza',
        'carros motos':'Carros e motos',
        'casamento':'Casamento',
        'celebridades':'Celebridades',
        'natureza':'Natureza',
        'ciência':'Ciência',
        'comida bebida':'Comidas e Bebidas',
        'decoração':'Decoração',
        'design':'Design',
        'educação':'Educação',
        'filme musica livro':'Entretenimento',
        'esporte':'Esporte',
        'festa evento feriado':'Festas, Feriados e Eventos',
        'fotografia':'Fotografia',
        'frase':'Frases',
        'geek':'Geek',
        'história':'História',
        'humor':'Humor',
        'ilustracao pôster':'Ilustrações e Pôsteres',
        'jardinagem':'Jardinagem',
        'homem moda':'Moda Masculina',
        'mulher moda':'Moda Feminina',
        'criança':'Pais e Filhos',
        'produto':'Produtos',
        'tattoos':'Tatuagens',
        'saúse':'Saúde e Boa forma',
        'tecnologia':'Tecnologia',
        'viagem':'Viagem',
        'outro':'Outros'
}

def permitido(name):
    return '.' in name and name.split('.')[-1].lower() in ['png','jpg','jpeg']

@pin.route('/inserir')
@login_required
def inserir():
    pasta_query = Pasta.query.filter_by(idcriador=session['user_id'])
    return render_template('inserirpin.html', plistar=pasta_query, options=options)

@pin.route('/salvar', methods=["GET", "POST"])
@login_required
def salvar():
    if request.method == 'POST':
      
        idpasta = int(request.form['pasta'])    
        idpin = int(request.form['pin'])

        pasta = Pasta.query.get(idpasta)
        pin = Pin.query.get(idpin)

        pasta.pins.append(pin)
        pasta.salva()

        return redirect(url_for('usuario.listarpins'))
    return render_template('index.html')

@pin.route('/buscar', methods=['GET'])
def buscar():
    id = int(request.values['id'])
    pin = Pin.query.get(id)
    return jsonify(pin = json.dumps(pin.toDict()))

@pin.route('/cadastrar', methods=["GET", "POST"])
@login_required
def cadastrar():
    if request.method == 'POST':
        titulo = request.form["titulo"]
        descricao = request.form["descricao"]
        imagem = request.files["imagem"]
        tematica = request.form["tematica"]
        idcriador = session['user_id']
        idpasta = int(request.form['pasta'])    
        pasta = Pasta.query.get(idpasta)

        if(request.values.has_key('id')):
            id = int(request.form['id'])
            pin = Pin.query.get(id)
            #pin.id = id
            #pin.salva()
            print(pin.pastaorigem)
            print(pasta)
            if(pin.pastaorigem != pasta):
                pasta.pins.append(pin)
            pin.titulo = titulo
            pin.descricao = descricao
            pin.tematica = tematica
            pin.idcriador = idcriador
            pin.data_atualizacao = datetime.now()
        else:
            pin = Pin(titulo=titulo, descricao=descricao, tematica=tematica, idcriador=idcriador, data_atualizacao=datetime.now())
            pasta.pins.append(pin)

        pin.pastaorigem = pasta
        #pin.idpastaorigem = pasta.id
        pin.salva()
        pasta.salva()

        if imagem and permitido(imagem.filename):
            extensao = imagem.filename.split('.')[-1].lower()
            nome_arquivo = secure_filename("{}.{}".format(pin.id, extensao))
            assembly = os.path.join('./pintarest/static', app.config['UPLOAD_FOLDER'], 'pins', nome_arquivo)

            if(request.values.has_key('foto')):
                foto = request.form['foto']
                if(foto == nome_arquivo):
                    os.remove(os.path.join(assembly))
            
            imagem.save(assembly)
            pin.data_atualizacao = datetime.now()
            pin.imagem = nome_arquivo
            pin.salva()

        return redirect(url_for('usuario.listarpins'))
    return render_template('index.html')

@pin.route('/update/<id>', methods=["GET", "POST"])
@login_required
def update():
    if request.method == 'POST':
        pin = Pin()
        pin = Pin.query.filter_by(id=id).first()
        
        pin.titulo = request.form['novo_titulo']
        pin.imagem = request.file['nova_imagem'].filename
        pin.descricao = request.form["nova_descricao"]
        pin.tematica = request.form["nova_tematica"]
        
        db.session.commit()
        return redirect(url_for('usuario.listarpins'))

@pin.route('/delete', methods=["GET"])
@login_required
def delete():
    id = int(request.values["id"])
    pin = Pin.query.get(id)
    pin.excluir()
    return redirect(url_for('usuario.listarpins'))

@pin.route('/editar', methods=['GET'])
@login_required
def editar():
    id = int(request.values["id"])
    pin = Pin.query.get(id)
    pasta_query = Pasta.query.filter_by(idcriador=session['user_id'])
    return render_template('inserirpin.html', plistar=pasta_query, pin=pin, options=options)