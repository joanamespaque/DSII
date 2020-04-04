from flask import Flask, render_template, request, session, redirect, url_for, Blueprint 
mensagem_bp = Blueprint('mensagem', __name__,url_prefix='/mensagem') 

@mensagem_bp.route('/')
def mensagem():
    msg = request.values['msg']
    if(request.values.has_key("link") == True):
        link = request.values['link']
        return render_template('mensagem.html', msg = msg, link = link)
    else:
        return render_template('mensagem.html', msg = msg)
