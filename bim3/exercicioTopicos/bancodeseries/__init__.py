__version__ = '0.1'
from flask import Flask, Blueprint

app = Flask('bancodeseries')
app.config['SECRET_KEY'] = 'alohomora'
app.debug = True 

from bancodeseries.controllers import *