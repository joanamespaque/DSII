from flask import Flask, Blueprint, request, render_template, redirect
from .. import db
from .. models.endereco import Endereco

endereco = Blueprint('endereco', __name__, url_prefix='/endereco')

@endereco.route('/listar')
def listar():
    enderecos = Endereco.query.all()
    return render_template('lista.html', enderecos=enderecos)

# (_,_)




