from flask import Flask, flash, render_template, request, session, redirect, url_for, Blueprint, jsonify
import json
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from bancodeseries import app
from bancodeseries.models.usuario import Usuario
from bancodeseries.models.usuarioDAO import UsuarioDAO
from bancodeseries.models.serieDAO import SerieDAO
from bancodeseries.models.serie import Serie
from bancodeseries.models.temporadaDAO import TemporadaDAO
from bancodeseries.models.temporada import Temporada
from bancodeseries.models.episodioDAO import EpisodioDAO
from bancodeseries.models.episodio import Episodio

episodio_bp = Blueprint('episodio', __name__, url_prefix='/episodio')

@episodio_bp.route('/telaInserir')
def telaInserir():
    series = SerieDAO().listar(50,0)
    return render_template('formEpisodio.html', series=series)

@episodio_bp.route('/salvar', methods=['POST'])
def salvar():
    titulo = request.form['titulo']
    codSerie = request.form['serie']
    codTemporada = request.form['temporada']
    serie = SerieDAO().buscar(Serie(cod = codSerie))
    temporada = TemporadaDAO().buscar(Temporada(cod = codTemporada))
    episodio = Episodio(titulo = titulo, serie = serie, temporada = temporada)
    if(request.values.has_key('cod')):
        cod = request.form['cod']
        episodio.cod = int(cod)
    EpisodioDAO().salvar(episodio)
    temporadas = TemporadaDAO().listar(serie, 50, 0)
    return render_template('serie.html', serie=serie, temporadas=temporadas)



@episodio_bp.route('/listar', methods=['GET'])
def listar():
    codTemporada = request.values['cod']
    temporada = TemporadaDAO().buscar(Temporada(cod=codTemporada))
    episodios = EpisodioDAO().listar(temporada, 50, 0)
    return jsonify(episodios = json.dumps(toDict(episodios)), temporada = json.dumps(temporada.toDict()))

@episodio_bp.route('/listaTemporadas', methods=['GET'])
def listarTemporadas():
    codSerie = request.values['cod']
    serie = SerieDAO().buscar(Serie(cod=codSerie))
    temporadas = TemporadaDAO().listar(serie, 50, 0)
    return jsonify(temporadas = json.dumps(toDict(temporadas)))

def toDict(lista):
    dict = {}
    for chave, objeto in enumerate(lista):
        newDict = {
            'cod': objeto.cod,
            'titulo': objeto.titulo,
            'numero': objeto.numero 
        }
        dict[chave] = newDict
    return dict
