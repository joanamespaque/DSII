from flask import Flask, Blueprint, request, render_template, redirect
from .. models.autor import Autor
from .. models.livro import Livro
from .. import db
import datetime

livro = Blueprint('livro', __name__, url_prefix='/livro')

@livro.route('/telaInserir')
def telaInserir():
    autores = Autor.query.all()
    return render_template('livro.html', autores=autores)

@livro.route('/inserir', methods=['POST', 'GET'])
def inserir():
    idsAutores = request.form.getlist('autores')
    if(idsAutores == []):
        autores = Autor.query.all()
        return render_template('livro.html', autores=autores, msg='Você precisa vincular no minimo um autor')
    else:
        titulo = request.form['titulo']
        data = request.form['data_lancamento']
        editora = request.form['editora']
        livro = Livro(titulo = titulo, data_lancamento=data, editora=editora)
        livro.insert(idsAutores)
        return redirect("/livro/listar")

@livro.route('/excluir', methods=['GET'])
def excluir():
    id = request.values['id']
    livro = Livro.query.get(id)
    livro.excluir()
    return redirect("/livro/listar")

@livro.route('/telaInfo', methods=['GET'])
def telaInfo():
    id = request.values['id']
    livro = Livro.query.get(id)
    return render_template('infoLivro.html', livro=livro)

@livro.route('/listar')
def listar():
    livros = Livro.query.all()
    return render_template('lista.html', livros=livros)
