from flask import Flask, Blueprint, request, render_template, redirect, url_for, session
from .. models.usuario import Usuario
from .. models.pasta import Pasta
from .. models.pasta import pasta_pin
from .. models.pin import Pin
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from .. import db
from hashlib import md5 
from ...pintarest import app
from sqlalchemy import text
from sqlalchemy import or_
import json, os


usuario = Blueprint('usuario', __name__, url_prefix='/usuario')
s = URLSafeTimedSerializer('alohomora')
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'usuario.geraTelaLogin'

@usuario.route('/cadastro')
def geraTelaCadastro():
    return render_template('cadastrar.html')

@usuario.route('/confirm_email/<token>', methods=['GET'])
def confirma_email(token):
    id = int(request.values["id"])
    busca = Usuario.query.filter_by(id=id).first()
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
            return render_template('cadastrar.html', msg = msg)
        else:
            msg = 'Você já validou seu e-mail.'

    if(busca.validado == True):
        msg = 'Você já validou seu e-mail.'
    else:
        msg = 'Seu e-mail foi validado, tetahead! Agora você já pode fazer login!'
        busca.validaUsuario()
    return render_template('entrar.html', msg=msg)

@usuario.route('/cadastrar', methods=['POST'])
def cadastrar():
    username = request.form["username"]
    usuarios = Usuario.query.all()
    email = request.form["email"].lower()
    for u in usuarios:
        if u.username.lower() == username.lower():
            return render_template("cadastrar.html", msg="Username já cadastrado. Tente outra opção.")
        if u.email.lower() == email:
            return render_template("cadastrar.html", msg="E-mail já cadastrado. Tente outra opção.")
    nome = request.form["nome"]
    senha = md5(request.form['senha'].encode('utf-8')).hexdigest()
    user = Usuario(nome=nome, email=email, username=username, senha=senha, validado=False, foto='profile.png')
    user.salvar()
    msg = Message('Confirme seu e-mail', sender='exerciciotesteds2@gmail.com', recipients=[email])
    link = geraToken(user)
    msg.body = 'Se você não confirmar o e-mail em uma hora o token expira!. Seu link:{}'.format(link)
    mail = Mail(app)
    mail.send(msg)
    return render_template('index.html', msg="Cadastro feito. Verifique seu e-mail para confirma-lo.")

def geraToken(usuario):
    token = s.dumps(usuario.email, salt='email-confirm')
    link = url_for('usuario.confirma_email', token=token, id=usuario.id, _external=True)
    return link

@usuario.route('/entrar')
def geraTelaLogin():
    return render_template('entrar.html')

@login_manager.user_loader
def load_user(user_id):
    try:
        return Usuario.query.filter_by(id=user_id).first()
    except models.DoesNotExist:
        return None

@usuario.route("/seguir", methods=['GET'])
def seguir_usuario():
    idseguido = int(request.values['id'])
    idseguidor = int(current_user.id)
    user_seguido = Usuario.query.get(idseguido)
    user_seguidor = Usuario.query.get(idseguidor)
    user_seguido.seguidores.append(user_seguidor)
    user_seguido.salvar()
    return redirect("/usuario/visualizar-perfil?id="+str(idseguido))

@usuario.route("/deixar_de_seguir", methods=['GET'])
def deixar_de_seguir_usuario():
    idseguido = int(request.values['id'])
    idseguidor = int(current_user.id)
    user_seguido = Usuario.query.get(idseguido)
    user_seguidor = Usuario.query.get(idseguidor)
    user_seguido.seguidores.remove(user_seguidor)
    user_seguido.salvar()
    return redirect("/usuario/visualizar-perfil?id="+str(idseguido))



@usuario.route('/login', methods=['GET', 'POST'])
def login():
    email = request.form['email'].lower()
    senha = md5(request.form['senha'].encode()).hexdigest()
    usuario = Usuario.query.filter_by(email=email).first()
    if usuario:
        if usuario.validado == True:
            if usuario.senha == senha:
                login_user(usuario, remember=True)
                return redirect('/')
        else:
            return render_template('entrar.html', msg='Você precisa validar seu e-mail para fazer login.')
    return render_template('entrar.html', msg='Login ou senha incorretos.')

@usuario.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

@usuario.route('/criar_pasta')
@login_required
def criar_pasta_modal():
    pasta_query = Pasta.query.filter_by(idcriador=session['user_id'])
    return render_template('pastas.html', plistar=pasta_query, mostramodal=True)

@usuario.route('/perfil')
@login_required
def perfil():
    return render_template('perfil.html')

@usuario.route('/pastas', methods=["GET"])
@login_required
def listarpastas():
    pasta_query = Pasta.query.filter_by(idcriador=session['user_id']).order_by(Pasta.data_atualizacao.desc())
    return render_template('pastas.html', plistar=pasta_query)

@usuario.route('/pins', methods=["GET"])
@login_required
def listarpins():
    pin_query = Pin.query.filter_by(idcriador=session['user_id']).order_by(Pin.data_atualizacao.desc())
    pasta_query = Pasta.query.filter_by(idcriador=session['user_id']).order_by(Pasta.data_atualizacao.desc())
    print(pin_query)
    return render_template('pins.html', plistar=pin_query, pastas=pasta_query)

@usuario.route('/usuarios')
def usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuarios.html', usuarios=usuarios)

@usuario.route('/pasta', methods=['GET'])
def pasta():
    id = int(request.values['id'])
    pasta = Pasta.query.get(id)
    return render_template('pastainfo.html', pasta=pasta)

@usuario.route('/pesquisar', methods=["POST"])
def pesquisar():
    text = request.form['pesquisa']
    pesquisa = request.form['tipo']
    search = "%{}%".format(text)
    # print(search)
    if(pesquisa == "pastas"):
        response = Pasta.query.filter(Pasta.nome.ilike(search)).filter(Pasta.secreto==False).order_by(Pasta.data_atualizacao.desc())
    elif(pesquisa=="pins"):
        response = Pasta.query.filter(Pasta.secreto == False).join(Pasta.pins).filter(or_(Pin.titulo.ilike(search), Pin.tematica.ilike(search))).order_by(Pin.data_atualizacao.desc())
    else:
        response = Usuario.query.filter(or_(Usuario.nome.ilike(search), Usuario.username.ilike(search)), Usuario.validado == True)

    return render_template('pesquisa.html', query=response, tipo=pesquisa)

@usuario.route("/buscar", methods=['GET'])
@login_required
def buscar():
    id = int(request.values['id'])
    usuario = Usuario.query.get(id)
    return jsonify(usuario = json.dumps(usuario.toDict()))

@usuario.route('/alterar_senha', methods=['GET', 'POST'])
@login_required
def alterar_senha():
    id = int(request.form['id'])
    usuario = Usuario.query.get(id)
    novasenha1 = md5(request.form['nova-senha1'].encode('utf-8')).hexdigest()
    novasenha2 = md5(request.form['nova-senha2'].encode('utf-8')).hexdigest()
    senhaantiga = md5(request.form['senha-antiga'].encode('utf-8')).hexdigest()
    if(senhaantiga == usuario.senha and novasenha1 == novasenha2 and novasenha1 == senhaantiga):
        msg = "A nova senha não pode ser igual a antiga."
    elif(novasenha1 == novasenha2):
        if(senhaantiga == usuario.senha):
            usuario.senha = novasenha1
            usuario.salvar()
            msg = "Senha alterada com sucesso."
        else:
            #senha errada
            msg = "Você digitou a senha errada :("
    elif(senhaantiga == usuario.senha):
        #as senhas nao combinam
        msg = "As senhas não combinam :o"
    else:
        #as senhas nao combinam e a senha antiga ta errada
        msg = "As senhas não combinam e você digitou sua senha errado :P"
    
    return render_template('perfil.html', msg=msg)

@usuario.route("/tela_excluir")
@login_required
def tela_excluir():
    return render_template('excluir.html')

@usuario.route("visualizar-perfil", methods=['GET'])
def visualizar_perfil():
    id = int(request.values['id'])
    if(id == current_user.id):
        return redirect('/usuario/pins')
    else:
        usuario = Usuario.query.get(id)
        pastas = Pasta.query.filter(Pasta.idcriador==id).filter(Pasta.secreto == False)
        if usuario in current_user.seguidos:
            seguido = True
        else:
            seguido = False
        return render_template("perfil-view.html", usuario = usuario, pastas=pastas, seguido=seguido)

@usuario.route("/excluir", methods=["POST"])
@login_required
def excluir():
    id = request.form['id']
    senha = md5(request.form['senha'].encode('utf-8')).hexdigest()
    usuario = Usuario.query.get(id)
    if(senha == usuario.senha):
        logout_user()
        usuario.excluir()
        return redirect('/')
    else:
        return render_template("excluir.html", msg='Senha errada.from werkzeug.utils import secure_filename')

@usuario.route("/editar_perfil", methods=['GET', 'POST'])
@login_required
def editar_perfil():
    id = request.form['id']
    usuario = Usuario.query.get(id)
    if(request.values.has_key('email')):
        usuario.email = request.form['email']
    else:
        nome = request.form['nome']
        username = request.form['username']
        imagem = request.files['foto']
        usuario.nome = nome
        usuario.username = username

        if imagem and permitido(imagem.filename):
            extensao = imagem.filename.split('.')[-1].lower()
            nome_arquivo = secure_filename("{}.{}".format(usuario.id, extensao))
            assembly = os.path.join('./pintarest/static', app.config['UPLOAD_FOLDER'], 'usuarios', nome_arquivo)
            try:
                os.remove(os.path.join(assembly))
                imagem.save(assembly)
            except FileNotFoundError:
                imagem.save(assembly)
            usuario.foto = nome_arquivo
    usuario.salvar()
    return render_template("perfil.html", msg="Informações salvas com sucesso.")


def permitido(name):
    return '.' in name and name.split('.')[-1].lower() in ['png','jpg','jpeg']

@usuario.route("/seguindo/usuarios", methods=['GET'])
# @login_required
def seguindo_users():
    id = int(request.values['id'])
    usuario = Usuario.query.get(id)
    pin = Pin.query.all()
    q = Pasta.query.all()
    return render_template("seguindo.html", usuarios=usuario.seguidos, usuario=usuario, pins=pin, query=q)

@usuario.route("/seguindo/pastas", methods=['GET'])
# @login_required
def seguindo_pastas():
    id = int(request.values['id'])
    usuario = Usuario.query.get(id)
    return render_template("seguindo.html", pastas=usuario.pastasSeguidas, usuario=usuario)