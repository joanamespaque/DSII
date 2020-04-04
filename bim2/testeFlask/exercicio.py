# -uma rota que recebe um parametro int e imprime os dados de 1 funcionario, considerando a classe Funcionario e FuncionarioDAO do exercicio anterior
from flask import Flask 
from FuncionarioDAO import *

app = Flask(__name__)

@app.route('/exercicio/<int:var>')
def trata_teste(var):
    # print("Oi")
    dao = FuncionarioDAO()
    s = dao.buscar(var)
    return s.__str__()

def main():
    app.env = "development"
    app.run(debug=True, port=5000)


if __name__ == '__main__':
    main()