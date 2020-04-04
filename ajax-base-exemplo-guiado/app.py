from flask import Flask, jsonify, render_template, request
from filmedao import *
import json
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
    id = int(request.values['id'])
    filme = dao.buscar(id)
    return jsonify(filme = json.dumps(filme.toDict()))

def main():
    app.env = 'development'
    app.run(debug=True)

if(__name__ == '__main__'):
    main()
