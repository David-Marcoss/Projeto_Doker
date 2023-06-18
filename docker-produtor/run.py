from  flask  import  Flask , request
from flask import render_template
from src.config.publisher import RabbitmqPublisher

app  =  Flask( __name__ )

@app.route ( '/' ) 
def  hello_world(): 
    return  'Hello World!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name="david")

@app.route('/insert/',methods=["POST","GET"])
def get_data():
    if request.method == "POST":
        cep = request.form["cep"]

        rabbitmq_publisher = RabbitmqPublisher()
        rabbitmq_publisher.send_message(cep)

        return  f'cep {cep}'
    
    return render_template('home.html')


if  __name__  ==  '__main__' : 
    app.run()