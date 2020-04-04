from flask import Flask, jsonify, render_template, request, jsonify
from filmedao import *
import simplejson
import time

app = Flask(__name__)

dao = FilmeDAO()

@app.route('/', methods=['POST', 'GET'])
def listar():
    filmes = dao.listar(10,0) 
    return render_template('lista.html', filmes = filmes)

@app.route('/buscar', methods=['GET'])
def buscar():
    time.sleep(3)
    # print('entrei na req OMO dupla acao!') LEMBRAR DE TIRAR ISSO DO CÓDIGO
    f_id = int(request.values["id"])  
    filme = dao.buscar(f_id) 
    return jsonify({'result':'success', 'filme': simplejson.dumps(filme.toDict())})

def main():
    app.env = 'development'
    app.run(debug=True)

if(__name__ == '__main__'):
    main()
