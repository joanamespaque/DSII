from flask_wtf import Form 
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import *
from wtforms.validators import InputRequired
class SerieForm(Form):
    titulo = StringField('Título:', validators=[InputRequired()])
    foto = FileField('Foto:', validators=[InputRequired()])
    enviar = SubmitField("Enviar")
