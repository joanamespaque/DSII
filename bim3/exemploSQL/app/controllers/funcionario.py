from flask import Flask, Blueprint, request, render_template, redirect
from .. models.departamento import Departamento
from .. models.funcionario import Funcionario
from .. import db

func = Blueprint('funcionario', __name__, url_prefix='/funcionario')

@func.route('/telaCadastro')
def telaCadastro():
    deptos = Departamento.query.all()
    return render_template('funcionario.html', departamentos=deptos)

# (_,_)

@func.route('/salvar', methods=['POST', 'GET'])
def salvar():
    nome = request.form['nome']
    iddepto = request.form['departamento']
    f = Funcionario(nome=nome, iddepto = iddepto)
    if(request.values.has_key('id')):
        f.id = request.form['id']
    f.salva()
    return redirect("/funcionario/listar")

@func.route('/excluir',  methods=['GET'])
def excluir():
    id = request.values['id']
    d = Funcionario.query.get(id)
    d.excluir()
    return redirect("/funcionario/listar")
    
@func.route('/alterar',  methods=['GET'])
def alterar():
    id = request.values['id']
    funcionario = Funcionario.query.get(id)
    deptos = Departamento.query.all()
    return render_template('funcionario.html', func=funcionario, departamentos = deptos)

@func.route('/listar')
def listar():
    funcionarios = Funcionario.query.all()
    return render_template('lista.html', funcionarios=funcionarios)
