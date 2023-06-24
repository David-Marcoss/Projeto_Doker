from  flask  import  Flask,request,render_template
import requests

app  =  Flask( __name__ )
 
@app.route('/',methods=["POST","GET"])
def get_data():
    if request.method == "POST":
        
        cep = request.form.get('cep')

        return  requests.post("http://172.19.0.6:5000",json={"cep":cep}).text
    
 
    return render_template("home.html")
    
    


if  __name__  ==  '__main__' : 
    app.run()