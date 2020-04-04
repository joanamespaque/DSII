# -uma rota que recebe um parametro int e imprime os dados de 1 funcionario, considerando a classe Funcionario e FuncionarioDAO do exercicio anterior
from flask import Flask 
from FuncionarioDAO import *

app = Flask(__name__)
app.run()


@app.route('/exercicio/<int:var>')
def trata_teste(var):
    dao = FuncionarioDAO()
    return dao.buscar(var)

def main():
    app.run()


if __name__=="__main__":
    main()
