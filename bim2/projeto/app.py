from ideiadao import *
from usuariodao import *
from flask import Flask, redirect, url_for, render_template, request, session
import hashlib

app = Flask(__name__)
rota = ['/', '/login']

@app.before_request #decorador
def before_request():
    # if(not session['logged_in']):
    if 'logged_in' not in session:
        if(not rota.__contains__(request.path)):
            return render_template("telaLogin.html")
    elif(rota.__contains__(request.path)):
        return redirect('/ideia/listar')

daoI = IdeiaDao()
daoU = UsuarioDao()

@app.route('/')
def telaLogin():
    return render_template('telaLogin.html')

@app.route('/logout')
def logout():
    session.pop('nome')
    session.pop('login')
    session['logged_in'] = False
    return redirect("/")

@app.route('/login', methods=['POST'])
def login():
    login = request.form['login']
    senha = hashlib.md5(request.form['senha'].encode()).hexdigest()
    usuario = Usuario(login=login, senha=senha)
    if(daoU.buscar(usuario)):
        u = daoU.buscar(usuario)
        session['logged_in'] = True
        session['nome'] = u.nome
        session['cod'] = u.cod
        session['login'] = u.login
        return render_template('nav.html')
    else:
        return render_template("telaLogin.html", erro="Senha e/ou login incorreto")

@app.route('/ideia/listar', methods=['POST', 'GET'])
def listarIdeias():
    ideias = daoI.listar(50, 0)
    total = len(ideias)
    return render_template('lista.html', ideias=ideias, len=total)

@app.route('/ideia/telaInserir', methods=["POST", "GET"])
def telaInserir():
    return render_template('inserirIdeia.html')

@app.route('/ideia/alterar', methods=['GET'])
def alterarProjeto():
    codAlterar = int(request.values["cod"])  
    ideia = daoI.buscar(codAlterar)
    if(session['login'] == ideia.usuario.login):
        return render_template('inserirIdeia.html', ideia=ideia)
    else:
        return redirect('/ideia/listar')

@app.route('/ideia/salvar', methods=['POST', 'GET'])
def salvarIdeia():  
    titulo = request.form["titulo"]
    descricao = request.form["descricao"]
    usuario = Usuario(nome=session['nome'], login=session['login'] )
    usuario.cod = session['cod']
    ideia = Ideia(titulo = titulo, descricao = descricao, usuario = usuario)
    if(request.values.has_key("cod") == True):
        cod = request.form["cod"]
        ideia.cod = int(cod)
        datahoraatualizacao = request.form['datahoraatualizacao']
        ideia.datahoraatualizacao = datahoraatualizacao
    daoI.salvar(ideia)
    return redirect("/ideia/listar")

@app.route('/ideia/excluir', methods=['GET'])
def excluirIdeia():
    cod = int(request.values["cod"])
    ideia = daoI.buscar(cod)
    if(ideia.usuario.login == session['login']):
        daoI.excluir(ideia)
    return redirect("/ideia/listar")

@app.route('/ideia/telaInfo', methods=['GET'])
def infoFuncionario():
    cod = int(request.values["cod"])  
    ideia = daoI.buscar(cod)
    return render_template('telaInfo.html', ideia=ideia)

def main(): 
    app.env = 'development'
    app.secret_key = "alohomora"
    app.run(debug = True, port = 5000)

if __name__ == '__main__': 
    main()