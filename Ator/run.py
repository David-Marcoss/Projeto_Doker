import sys
from  flask  import  Flask,request,render_template
import requests

app  =  Flask( __name__ )
 
@app.route('/',methods=["POST","GET"])
def get_data():
    if request.method == "POST":
        
        cep = request.form.get('cep')
        
        print(f'{cep}:Dado enviado para o produtor !!\n', file=sys.stderr)

        try:

            return  requests.post("http://docker-produtor:5000/",json={"cep":cep}).text
        except:
            return "Status: 404 Não foi possivel conectar com o servidor!!"
    
 
    return render_template("home.html")
    
    


if  __name__  ==  '__main__' : 
    app.run()