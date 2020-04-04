from Flask import session 

@app.before_first_request
def before_firts_request():
    print("before_first_request() chamando...")
@app.before_request 
def before_request():
    print(request.path)
    print("before_request() chamando...")

@app.after_request 
def after_request():
    print(request.path)
    print("after_request() chamando...")


def main():
    app.env = 'development'
    app.secret_key = "chave secreta"
    app.run()