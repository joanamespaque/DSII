from flask import Flask, Blueprint, request, render_template, redirect
from .. models.departamento import Departamento
from .. models.endereco import Endereco
from .. import db

depto = Blueprint('depto', __name__, url_prefix='/depto')

@depto.route('/telaCadastro')
def telaCadastro():
    return render_template('departamento.html')

# (_,_)

@depto.route('/salvar', methods=['POST', 'GET'])
def salvar():
    nome = request.form['nome']
    rua = request.form['rua']
    numero = request.form['numero']
    d = Departamento(nome=nome)
    e = Endereco(rua=rua, numero=numero)
    if(request.values.has_key('id')):
        d.id = request.form['id']
        e.id = request.form['idEndereco']
    e.salva()
    d.endereco = e
    d.salva()
    return redirect("/depto/listar")

@depto.route('/excluir', methods=['GET'])
def excluir():
    id = request.values['id']
    d = Departamento.query.get(id)
    print(d)
    print(id)
    print("11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")
    d.excluir()
    return redirect("/depto/listar")
    
@depto.route('/alterar',  methods=['GET'])
def alterar():
    id = request.values['id']
    depto = Departamento.query.get(id)
    return render_template('departamento.html', depto=depto)

@depto.route('/listar')
def listar():
    deptos = Departamento.query.all()
    return render_template('lista.html', departamentos=deptos)
