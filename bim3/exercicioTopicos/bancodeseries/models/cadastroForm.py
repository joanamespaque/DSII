from flask_wtf import FlaskForm 
from wtforms import validators, StringField, PasswordField, SubmitField, FloatField, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms.validators import *
from wtforms.widgets.html5 import NumberInput
from wtforms.validators import InputRequired

class CadastroForm(FlaskForm):
    nome = StringField('Nome:', validators=[InputRequired()])
    login = StringField('Login:', validators=[InputRequired()])
    email = StringField("Email",  [InputRequired("Please enter your email address."), Email("This field requires a valid email address")])
    altura = FloatField('Altura:', validators=[InputRequired()], widget=NumberInput(step=.01, max=3))
    idade = IntegerField('Idade:',  validators=[InputRequired()], widget=NumberInput())
    senha = PasswordField('Senha:', validators=[InputRequired()])
    enviar = SubmitField("Enviar")