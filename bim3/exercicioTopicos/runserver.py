import os 
from bancodeseries import app 
from flask import Blueprint, session, request, redirect, render_template, url_for
from bancodeseries.controllers.usuario_bp import usuario_bp
from bancodeseries.controllers.mensagem_bp import mensagem_bp
from bancodeseries.controllers.serie_bp import serie_bp
from bancodeseries.controllers.temporada_bp import temporada_bp
from bancodeseries.controllers.episodio_bp import episodio_bp
from bancodeseries.models.serieDAO import SerieDAO
app.register_blueprint(usuario_bp)
app.register_blueprint(mensagem_bp)
app.register_blueprint(serie_bp)
app.register_blueprint(temporada_bp)
app.register_blueprint(episodio_bp)

rota = ['/usuario/telaCadastro', '/usuario/telaLogin', '/usuario/login', '/usuario/cadastro']
@app.before_request #decorador
def before_request():
    series = SerieDAO().listar(50, 0)
    if 'login' not in session:
        if(request.path == "/serie/listar"):
            return render_template('lista.html', series=series)
        elif(not rota.__contains__(request.path)):
            return redirect('/usuario/telaLogin')
    elif(rota.__contains__(request.path)):
        return render_template('lista.html', series=series)

@app.before_first_request
def init_fun():
    if not os.path.isdir(os.path.join('bancodeseries', 'static')):
        os.mkdir(os.path.join('./bancodeseries/static'))
        if not os.path.isdir(os.path.join('bancodeseries', 'static', 'uploads')):
            os.mkdir(os.path.join('./bancodeseries/static', 'uploads'))

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_USERNAME='exerciciotesteds2@gmail.com',
    MAIL_DEFAULT_SENDER='exerciciotesteds2@gmail.com',
    MAIL_PASSWORD='vishmarinamail',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USE_TLS=False,
    UPLOAD_FOLDER='uploads'
))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.env = 'development'
    app.run('localhost', port = port)
    