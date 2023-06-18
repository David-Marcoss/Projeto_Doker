from  flask  import  Flask , request
from flask import render_template
from src.config.publisher import RabbitmqPublisher

app  =  Flask( __name__ )
 
@app.route('/',methods=["POST","GET"])
def get_data():
    if request.method == "POST":
        cep = request.form["cep"]

        rabbitmq_publisher = RabbitmqPublisher()
        rabbitmq_publisher.send_message(cep)

        return  f'Requisição enviada com sucesso!!'
    
    return render_template('home.html')


if  __name__  ==  '__main__' : 
    app.run()