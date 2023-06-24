from  flask  import  Flask , request
from flask import render_template
from src.config.publisher import RabbitmqPublisher

app  =  Flask( __name__ )
 
@app.route('/',methods=["POST","GET"])
def get_data():
    if request.method == "POST":
        request_data = request.get_json()

        cep = request_data["cep"]

        rabbitmq_publisher = RabbitmqPublisher()
        rabbitmq_publisher.send_message(cep)

        return  f'Requisição enviada com sucesso!!'
    
    else:
        return "bad request !"
    
    


if  __name__  ==  '__main__' : 
    app.run()