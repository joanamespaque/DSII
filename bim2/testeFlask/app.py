from DepartamentoDAO import *
from datetime import datetime
import psycopg2
from flask import Flask, redirect, url_for, render_template, request, session
import hashlib
app = Flask(__name__)

daoD = DepartamentoDAO()
daoF = FuncionarioDAO()
daoP = ProjetoDAO()
rotasFunc = ['/projeto/listar', '/projeto/telaInserir', '/projeto/excluir', '/projeto/alterar', '/projeto/telaInfo', '/projeto/salvar']

# @app.before_request #decorador
# def before_request():
#     if ('logged_in' in session):
#         if(not session['adm']):
#             print(request.path)
#             if(not rotasFunc.__contains__(request.path)):
#                 return render_template(url_for('navAdm.html'))
#             else:
#                 return redirect(request.path)
#         else:
#             return redirect(request.path)
#     else:
#         return redirect((url_for('telalogin')))

# @app.after_request 
# def after_request(response):
#     print(request.path)
#     print("after_request() chamando...")
#     return response


@app.route('/')
def telaLogin():
    return render_template('telaLogin.html')

@app.route('/logout')
def logout():
    session.pop('nome')
    session.pop('adm')
    session['logged_in'] = False
    return redirect("/")

@app.route('/login', methods=['POST'])
def login():
    login = request.form['login'].lower()
    senha = hashlib.md5(request.form['senha'].lower().encode()).hexdigest()
    if(daoF.buscarLogin(login, senha)):
        funcionario = daoF.buscarLogin(login, senha)
        session['logged_in'] = True
        session['nome'] = funcionario.nome
        session['adm'] = funcionario.adm
        return render_template('lista.html')
    else:
        return render_template("telaLogin.html", erro="Senha e/ou login incorreto")

@app.route('/projeto/telaInserir', methods=["POST", "GET"])
def selectVinculaFuncionarios():
    funcionarios = daoF.listar()
    return render_template('inserirProjeto.html', funcionarios=funcionarios)

@app.route('/departamento/telaInserir', methods=["POST", "GET"])
def selectFuncionarios():
    funcionarios = daoF.listar()
    return render_template('inserirDepartamento.html', funcionarios=funcionarios)

@app.route('/funcionario/telaInserir', methods=["POST", "GET"])
def selectDepartamentos():
    departamentos = daoD.listar()
    return render_template('inserirFuncionario.html', departamentos=departamentos)

@app.route('/funcionario/telaInfo', methods=['GET'])
def infoFuncionario():
    cod = int(request.values["cod"])  
    funcionario = daoF.buscar(cod)
    return render_template('telaInfo.html', funcionario=funcionario)

@app.route('/projeto/telaInfo', methods=['GET'])
def infoProjeto():
    cod = int(request.values["cod"])  
    projeto = daoP.buscar(cod)
    funcionarios = projeto.funcionarios
    return render_template('telaInfo.html', projeto=projeto, funcionarios=funcionarios)

@app.route('/funcionario/alterar', methods=['GET'])
def alterarFuncionario():
    departamentos = daoD.listar()
    codAlterar = int(request.values["cod"])  
    funcionario = daoF.buscar(codAlterar)
    return render_template('inserirFuncionario.html', funcionario = funcionario, departamentos=departamentos)

@app.route('/departamento/alterar', methods=['GET'])
def alterarDepartamento():
    funcionarios = daoF.listar()
    codAlterar = int(request.values["cod"])  
    departamento = daoD.buscar(codAlterar)
    return render_template('inserirDepartamento.html', departamento = departamento, funcionarios = funcionarios)

@app.route('/projeto/alterar', methods=['GET'])
def alterarProjeto():
    funcionarios = daoF.listar()
    codAlterar = int(request.values["cod"])  
    projeto = daoP.buscar(codAlterar)
    # print(projeto.funcionarios)
    return render_template('inserirProjeto.html', projeto = projeto, funcionarios = funcionarios)

@app.route('/funcionario/salvar', methods=['POST', 'GET'])
def salvarFuncionario():  
    nome = request.form["nome"]
    login = request.form["login"].lower()
    senha = hashlib.md5(request.form["senha"].lower().encode()).hexdigest()
    adm = request.form["adm"]
    codDepto = int(request.form["departamento"])
    depto = daoD.buscar(codDepto)
    funcionario = Funcionario(nome, login, senha, adm)
    funcionario.departamento = depto
    if(request.values.has_key("funcCod") == True):
        cod = request.form["funcCod"]
        funcionario.cod = int(cod)
    daoF.salvar(funcionario)
    return redirect("/funcionario/listar")

@app.route('/departamento/salvar', methods=['POST', 'GET'])
def salvarDepartamento():  
    nome = request.form["nome"]
    depto = Departamento(nome)
    depto.dt_atu = datetime.now()
    depto.gerente = daoF.buscar(request.form["gerente"])
    if(request.values.has_key("deptoCod")):
        cod = request.form["deptoCod"]
        depto.cod = int(cod)
    daoD.salvar(depto)
    return redirect("/departamento/listar")

@app.route('/projeto/salvar', methods=['POST', 'GET'])
def salvarProjeto():  
    funcionarios = request.form.getlist('funcionario')
    nome = request.form["nome"]
    dataprevista = request.form['dataprevista']
    projeto = Projeto(nome, dataprevista)
    if(request.values.has_key("projcod")):
        cod = request.form["projcod"]
        projeto.cod = int(cod)
    i = 0 
    while(i < len(funcionarios)):
        func = daoF.buscar(int(funcionarios[i]))
        projeto.vinculaFuncionario(func)
        i+=1
    daoP.salvar(projeto)
    return redirect("/projeto/listar")

@app.route('/funcionario/listar', methods=['POST', 'GET'])
def listarFuncionarios():
    funcionarios = daoF.listar()
    total = len(funcionarios)
    return render_template('lista.html', funcionarios=funcionarios, len=total)

@app.route('/departamento/listar', methods=['POST', 'GET'])
def listarDepartamentos():
    departamentos = daoD.listar()
    total = len(departamentos)
    return render_template('lista.html', departamentos=departamentos, len=total)

@app.route('/projeto/listar', methods=['POST', 'GET'])
def listarProjetos():
    projetos = daoP.listar()
    total = len(projetos)
    return render_template('lista.html', projetos = projetos, len=total)

@app.route('/funcionario/excluir', methods=['GET'])
def excluirFuncionario():
    codFunc = int(request.values["cod"])
    daoF.excluir(codFunc)
    return redirect("/funcionario/listar")

@app.route('/departamento/excluir', methods=['GET'])
def excluirDepartamento():
    codDep = int(request.values["cod"])
    daoD.excluir(codDep)
    return redirect("/departamento/listar")

@app.route('/projeto/excluir', methods=['GET'])
def excluirProjeto():
    codProj = int(request.values["cod"])
    daoP.excluir(codProj)
    return redirect("/projeto/listar")

def main(): 
    app.env = 'development'
    app.secret_key = "alohomora"
    app.run(debug = True, port = 5000)

if __name__ == '__main__': 
    main()