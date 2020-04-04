from flask import Flask 
app = Flask(__name__)

@app.route('/')
def helloworld():
    return "ola mundao"

@app.route('/teste/<var>/<float:varf>')
def trata_teste(var, varf):
    print(type(var))
    print(type(varf))
    s = "var:{}<br>varf:{}".format(var, varf)
    return s

def main():
    app.env = "development"
    app.run(debug=True, port=2000)


if __name__ == '__main__':
    main()
#outra:

# set FLASK_APP = arquivo.py 
# flask ruin 

# set FLASK_ENV = development

#para ativar o AV:
# C:\Users\Fatima\testeDS\testeDS\Scripts>activate

# para executar o arquivo:
# executar o ambiente virtual
# entrar na pasta do arquivo 
# python arquivo.py
# from flask import render_template