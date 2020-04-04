from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField 
from wtforms.validators import *
from wtforms.validators import InputRequired
class LoginForm(Form):
    # login = StringField('Login:', validators=[input_required()])
    login = StringField('Login:', validators=[InputRequired()])
    senha = PasswordField('Senha:', validators=[InputRequired()])
    enviar = SubmitField("Enviar")
