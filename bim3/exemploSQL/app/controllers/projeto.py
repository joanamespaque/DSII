from flask import Flask, Blueprint, request, render_template, redirect
from .. models.funcionario import Funcionario
from .. models.projeto import Projeto
from .. import db

projeto = Blueprint('projeto', __name__, url_prefix='/projeto')

@projeto.route('/telaCadastro')
def telaCadastro():
    funcionarios = Funcionario.query.all()
    return render_template('projeto.html', funcionarios=funcionarios)

@projeto.route('/telaInfo', methods=['GET'])
def telaInfo():
    id = request.values['id']
    projeto = Projeto.query.get(id)
    return render_template('infoProjeto.html', projeto=projeto)

# (_,_)

@projeto.route('/salvar', methods=['POST', 'GET'])
def salvar():
    nome = request.form['nome']
    idsFuncionarios = request.form.getlist('funcionario')
    projeto = Projeto(nome=nome)
    if(request.values.has_key('id')):
        projeto.id = int(request.form['id'])
    projeto.salva(idsFuncionarios)
    return redirect("/projeto/listar")

@projeto.route('/excluir', methods=['GET'])
def excluir():
    id = request.values['id']
    projeto = Projeto.query.get(id)
    projeto.excluir()
    return redirect("/projeto/listar")
    
@projeto.route('/alterar', methods=['GET'])
def alterar():
    id = request.values['id']
    projeto = Projeto.query.get(id)
    funcionarios = Funcionario.query.all()
    return render_template('projeto.html', projeto=projeto, funcionarios=funcionarios)

@projeto.route('/listar')
def listar():
    projetos = Projeto.query.all()
    return render_template('lista.html', projetos=projetos)