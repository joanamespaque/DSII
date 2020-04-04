from flask import Flask, Blueprint, request, render_template, redirect
from .. models.departamento import Departamento
from .. import db

depto = Blueprint('depto', __name__, url_prefix='/depto')

@depto.route('/telaCadastro')
def telaCadastro():
    return render_template('formulario.html')

@depto.route('/salvar', methods=['POST', 'GET'])
def salvar():
    nome = request.form['nome']
    if(request.values.has_key('id')):
        id = request.form['id']
        d = Departamento.query.filter_by(id=id).first()
        d.nome = nome
        db.session.commit()
    else:
        d = Departamento(nome=nome)
        d.salva()
    return redirect("/depto/listar")

@depto.route('/excluir')
def excluir():
    id = request.values['id']
    d = Departamento.query.get(id)
    d.excluir()
    return redirect("/depto/listar")
    
@depto.route('/alterar')
def alterar():
    id = request.values['id']
    depto = Departamento.query.get(id)
    return render_template('formulario.html', depto=depto)

@depto.route('/listar')
def listar():
    deptos = Departamento.query.all()
    return render_template('lista.html', deptos=deptos)
