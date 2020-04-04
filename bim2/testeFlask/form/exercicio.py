#uma rota que recebe um parametro int e imprime os dados de um funcionário considerando a classe funcionário e FuncionarioDAO do exercicio anterior
from flask import Flask
# from flask import request
# from autordao import AutorDAO
# from autor import Autor
# from trabalhodao import TrabalhoDAO
# from trabalho import Trabalho
import psycopg2
from flask import render_template, request

app = Flask(__name__)


# @app.route('/<cod>')

# def busca_func(cod):
#     dao = AutorDAO()
#     autor = dao.buscar(cod)
#     print(autor)
#     return autor.__str__()




@app.route('/form')
def forms():
    return render_template('form.html')



@app.route('/formulario', methods=["POST", "GET"])
def trata_formulario():
    # print("nome")
    nome = request.form["nome"]
    var = int(request.form["departamento"])
    return render_template('testeFORM.html', nome = nome, var = var)





def main():
    app.env = 'development'
    app.run(debug = True, port = 5000)

if __name__ == '__main__': 
    main()


