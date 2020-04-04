from flask import Flask, render_template, request, session, redirect, url_for, Blueprint 
from hashlib import md5 
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from bancodeseries.models.usuario import Usuario
from bancodeseries.models.usuarioDAO import UsuarioDAO
from bancodeseries.models.cadastroForm import CadastroForm
from bancodeseries.models.loginForm import LoginForm
from bancodeseries import app

usuario_bp = Blueprint('usuario', __name__,url_prefix='/usuario') 
s = URLSafeTimedSerializer('alohomora')

@usuario_bp.route('/teste')
def teste():
    print(app.config)
    return app.config


@usuario_bp.route('/logout')
def logout():
    session.clear()
    return redirect("/")

@usuario_bp.route('/telaCadastro')
def telaCadastro():
    form = CadastroForm()
    if(request.values.has_key("msg") == True):
        msg = request.values['msg']
        return render_template('telaCadastro.html', form = form, msg = msg)
    else:
        return render_template('telaCadastro.html', form = form)

@usuario_bp.route('/telaLogin')
def telaLogin():
    form = LoginForm()
    return render_template('telaLogin.html', form = form)

@usuario_bp.route('/login', methods=['POST'])
def login():
    login = request.form['login']
    senha = md5(request.form['senha'].encode()).hexdigest()
    usuario = Usuario(login=login, senha=senha)
    if(UsuarioDAO().login(usuario)):
        u = UsuarioDAO().login(usuario)
        session['nome'] = u.nome
        session['cod'] = u.cod
        session['login'] = u.login
        return redirect('/serie/listar')
    else:
        form = LoginForm()
        return render_template('telaLogin.html', form = form, msg='Login ou senha incorretos.')


@usuario_bp.route('/confirm_email/<token>', methods=['GET'])
def confirma_email(token):
    cod = request.values["cod"]
    usuario = Usuario(cod=cod)
    busca = UsuarioDAO().buscar(usuario)
    try:
        email = s.loads(token, salt='email-confirm', max_age=3600)
    except SignatureExpired:
        if(busca.validado == False):
            msg = 'Seu token expirou e um novo foi enviado ao seu e-mail.'
            msgMail = Message('Novo token', sender='exerciciotesteds2@gmail.com', recipients=[email])
            link = geraToken(usuario)
            msg.body = 'Se você não confirmar o e-mail em uma hora o token expira novamente!. Seu link:{}'.format(link)
            mail = Mail(app)
            mail.send(msgMail)
            form = CadastroForm()
            return render_template('telaCadastro.html', form = form, msg = msg)
        else:
            msg = 'Você já validou seu e-mail.'

    if(busca.validado == True):
        msg = 'Você já validou seu e-mail.'
    else:
        msg = 'Seu e-mail foi validado, tetahead! Agora você já pode fazer login!'
        UsuarioDAO().validaUsuario(cod)
    form = LoginForm()
    return render_template('telaLogin.html', form = form, msg=msg)

@usuario_bp.route('/cadastro', methods=['POST'])
def cadastrar():
    nome = request.form["nome"]
    login = request.form["login"]
    email = request.form["email"]
    altura = request.form["altura"]
    idade = request.form["idade"]
    senha = md5(request.form['senha'].encode('utf-8')).hexdigest()
    user = Usuario(nome=nome, email=email, login=login, senha=senha, altura=altura, idade=idade)
    UsuarioDAO().inserir(user)
    msg = Message('Confirme seu e-mail', sender='exerciciotesteds2@gmail.com', recipients=[email])
    link = geraToken(user)
    msg.body = 'Se você não confirmar o e-mail em uma hora o token expira!. Seu link:{}'.format(link)
    mail = Mail(app)
    mail.send(msg)
    return redirect(url_for('mensagem.mensagem', msg='Seu cadastro foi feito. Verifique seu e-mail para validá-lo.', link = 'https://gmail.com/mail/'))
    # https://gmail.com/mail/

def geraToken(usuario):
    token = s.dumps(usuario.email, salt='email-confirm')
    link = url_for('usuario.confirma_email', token=token, cod=usuario.cod, _external=True)
    return link
