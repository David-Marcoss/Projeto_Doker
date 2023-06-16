from  flask  import  Flask , request
from flask import render_template
import requests
from src import enderecos_op


app  =  Flask( __name__ )

@app.route ( '/' ) 
def  hello_world(): 
    return  'Hello World!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name="david")

@app.route('/insert/',methods=["POST"])
def insert():

    #capturando requisição
    body = request.json
    cep = body['cep']

    print(body)
    
    #fazendo conexão com api externa
    req = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    endereco = req.json()

    if endereco != {'erro': True}:
        #inserindo os dados obtidos via api no bd
        op = enderecos_op()
        op.insert(endereco["cep"],endereco["logradouro"],endereco["bairro"],endereco["uf"])

        return "Operação concluida !!"
        
    else:
        return "Cep não encontrado!"




if  __name__  ==  '__main__' : 
    app.run()