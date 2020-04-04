from flask import Flask, flash, render_template, request, session, redirect, url_for, Blueprint 
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from bancodeseries import app
from bancodeseries.models.usuario import Usuario
from bancodeseries.models.usuarioDAO import UsuarioDAO
from bancodeseries.models.serieDAO import SerieDAO
from bancodeseries.models.serie import Serie
from bancodeseries.models.temporadaDAO import TemporadaDAO
from bancodeseries.models.temporada import Temporada

temporada_bp = Blueprint('temporada', __name__, url_prefix='/temporada')

@temporada_bp.route('/telaInserir')
def telaInserir():
    series = SerieDAO().listar(50,0)
    return render_template('formTemporada.html', series=series)

@temporada_bp.route('/alterar', methods=['GET'])
def alterar():
    codAlterar = int(request.values["cod"])  
    temporada = TemporadaDAO().buscar(Temporada(cod=codAlterar))
    series = SerieDAO().listar(50, 0)
    if(session['login'] == temporada.serie.usuario.login):
        return render_template('formTemporada.html', series=series, temporada=temporada)
    else:
        return redirect('/serie/listar')

@temporada_bp.route('excluir', methods=['GET'])
def excluir():
    cod = int(request.values['cod'])
    temporada = TemporadaDAO().buscar(Temporada(cod=cod))
    if(session['login'] == temporada.serie.usuario.login):
        TemporadaDAO().excluir(temporada)
        serie = temporada.serie
        temporadas = TemporadaDAO().listar(serie, 50, 0)
        return render_template('serie.html', serie=serie, temporadas=temporadas)
    else:
        return redirect('/serie/listar')
    

@temporada_bp.route('/salvar', methods=['POST'])
def salvar():
    titulo = request.form['titulo']
    codSerie = int(request.form['serie'])
    serie = SerieDAO().buscar(Serie(cod=codSerie))
    # usuario = UsuarioDAO().buscar(Usuario(cod=session['cod']))
    temporada = Temporada(titulo=titulo, serie=serie)
    if(request.values.has_key('cod')):
        cod = request.form['cod']
        temporada.cod = int(cod)
    TemporadaDAO().salvar(temporada)
    temporadas = TemporadaDAO().listar(serie, 50, 0)
    return render_template('serie.html', serie=serie, temporadas=temporadas)
