#oi brendinha, turu bom? coloquei alguns comentários pra tentar te ajudar bjks luminosas :)
from ideiadao import *
from usuariodao import *
from flask import Flask, redirect, url_for, render_template, request, session
import hashlib
app = Flask(__name__)
#essa lista "rota" tem as rotas que o usuario que nao esta logado pode acessar:
rota = ['/', '/login']

@app.before_request #decorador
def before_request():
    if 'login' not in session:
        #o if abaixo verifica se url que o usuario nao esta acessando está na lista de rotas, se nao estiver ele redireciona o usuario pra pagina de login pq ele eh baita abusado e nem logou ainda entao nao pode acessar o resto
        if(not rota.__contains__(request.path)):
            return render_template("telaLogin.html")
    #se entrar nesse elif quer dizer que ele esta logado, entao ele verifica se o usuario esta tentando acessar uma url/rota de login e nao deixa ele acessar 
    elif(rota.__contains__(request.path)):
        return redirect('/ideia/listar')

daoI = IdeiaDao()
daoU = UsuarioDao()
@app.route('/')
def telaLogin():
    return render_template('telaLogin.html')

@app.route('/logout')
def logout():
    #se nao for usar o clear, da de limpar a session dando pop na lista da seguinte forma:  (obs: o tiaguinhobd que colocou isso no código pra mim em um atendimento, se estiver errado a culpa é dele)
    #if 'nome' in session: session.pop('nome')
    #if 'login' in session: session.pop('login')
    session.clear()
    return redirect("/")

@app.route('/login', methods=['POST'])
def login():
    #pelo o que entendi, a gente usa request.form quando está pegando o value de um item do formulario e request.values quando está pegando um valor através da rota passada no teu formulario, como os ids pegos atraves do GET
    login = request.form['login']
    senha = hashlib.md5(request.form['senha'].encode()).hexdigest()
    usuario = Usuario(login=login, senha=senha)
    if(daoU.buscar(usuario)):
        u = daoU.buscar(usuario)
        session['nome'] = u.nome
        session['cod'] = u.cod
        session['login'] = u.login
        return redirect('/ideia/listar')
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
        print(cod)
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