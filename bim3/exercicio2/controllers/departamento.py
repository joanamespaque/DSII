from flask import Flask,render_template, request,session, redirect
from flask_sqlalchemy import SQLAlchemy

#from models.departamento import Departamento
#from models.endereco import Endereco
#from models.funcionario import Funcionario

app = Flask(__name__)


uri= 'postgresql://postgres:postgres@localhost:5432/exercicio'
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.init_app(app)


@app.route('/d/salvar',methods=["POST","GET"])
def depto_inserir():
    if request.method == "POST":
        d = Departamento()
        d.nome = request.form['nome']
        
        e = Endereco()
        e.numero = request.form['numero']
        e.rua = request.form['rua']

        coddepto=request.form["iddepartamento"]
        codendereco=request.form["idendereco"]

        if (coddepto):
            d.id=int(coddepto)
        
        if (codendereco):
            e.id=int(codendereco)

        d1=d
        e1=e

        e.salvar(e1)
        d.endereco = e

        d.salvar(d1)
        return redirect("/d/listar")

    return render_template('inserirDepartamento.html')


@app.route('/d/listar')
def deptoListar():
    l = Departamento.query.all()
    return render_template('listarDepartamentos.html',dlista=l)


@app.route('/d/editar/<id>')
def editarDepartamento(id):
    d = Departamento.query.get(id)
    return render_template('editarDepartamento.html',depto=d)


@app.route('/d/excluir/<id>')
def excluirDepartamento(id):
    d = Departamento()
    dbusca = Departamento.query.get(id)
    d.excluir(dbusca)
    return redirect("/d/listar")



