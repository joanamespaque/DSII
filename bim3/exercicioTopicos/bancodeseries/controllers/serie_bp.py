from flask import Flask, flash, render_template, request, session, redirect, url_for, Blueprint 
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from bancodeseries import app
from werkzeug.utils import secure_filename
from bancodeseries.models.usuario import Usuario
from bancodeseries.models.usuarioDAO import UsuarioDAO
from bancodeseries.models.serieDAO import SerieDAO
from bancodeseries.models.serie import Serie
from bancodeseries.models.temporadaDAO import TemporadaDAO
from bancodeseries.models.temporada import Temporada
from bancodeseries.models.serieForm import SerieForm
import os
serie_bp = Blueprint('serie', __name__,url_prefix='/serie')

def permitido(name):
    return '.' in name and name.split('.')[-1].lower() in ['jpg', 'png', 'jpeg']

@serie_bp.route('/detalhes', methods=['POST', 'GET'])
def telaDetalhes():
    cod = request.values["cod"]
    serie = SerieDAO().buscar(Serie(cod=cod))
    temporadas = TemporadaDAO().listar(serie, 50, 0)
    return render_template('serie.html', serie=serie, temporadas=temporadas)

@serie_bp.route('/listar', methods=['POST', 'GET'])
def listar():
    series = SerieDAO().listar(50, 0)
    return render_template('lista.html', series=series)

@serie_bp.route('/telaInserir')
def telaInserir():
    form = SerieForm()
    return render_template('formSerie.html', form=form)

@serie_bp.route('/alterar', methods=['GET'])
def alterar():
    codAlterar = int(request.values["cod"])  
    serie = SerieDAO().buscar(Serie(cod=codAlterar))
    form = SerieForm()
    if(session['login'] == serie.usuario.login):
        return render_template('formSerie.html', serie=serie, form=form)
    else:
        return redirect('/serie/listar')

@serie_bp.route('/excluir', methods=['GET'])
def excluir():
    cod = int(request.values["cod"])
    serie = SerieDAO().buscar(Serie(cod=cod))
    if(session['login'] == serie.usuario.login):
        os.remove(os.path.join('./bancodeseries/static', serie.foto))
        SerieDAO().excluir(serie)
    return redirect('/serie/listar')

@serie_bp.route('/salvar', methods=['POST', 'GET'])
def salvar():
    titulo = request.form["titulo"]
    arquivo = request.files['file']
    cod = session['cod']
    usuario = UsuarioDAO().buscar(Usuario(cod=cod))
    serie = Serie(titulo=titulo, usuario=usuario)

    if(request.values.has_key('cod')):
        cod = request.form['cod']
        serie.cod = int(cod) 

    SerieDAO().salvar(serie)

    if 'file' in request.files:
        if arquivo and permitido(arquivo.filename):
            extensao = arquivo.filename.split('.')[-1].lower()
            nome_arquivo = secure_filename("{}.{}".format(serie.cod, extensao))
            caminho = os.path.join(app.config['UPLOAD_FOLDER'], nome_arquivo)  
            if(request.values.has_key('foto')):
                foto = request.form['foto']
                if(foto == caminho):
                    os.remove(os.path.join('./bancodeseries/static', nome_arquivo))
            arquivo.save(os.path.join('./bancodeseries/static', app.config['UPLOAD_FOLDER'], nome_arquivo))
            serie.foto = caminho
            SerieDAO().salvar(serie)         

    return redirect("/serie/listar")

