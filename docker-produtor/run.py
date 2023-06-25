import sys
from  flask  import  Flask , request
from flask import render_template
from src.config.publisher import RabbitmqPublisher

app  =  Flask( __name__ )
 
@app.route('/',methods=["POST","GET"])
def get_data():
    if request.method == "POST":
        request_data = request.get_json()

        print(f"Requisição recebida: {request_data} ", file=sys.stderr)    

        cep = request_data["cep"]

        rabbitmq_publisher = RabbitmqPublisher()
        rabbitmq_publisher.send_message(cep)


        print('Dado enviado para a fila !!\n', file=sys.stderr)

        return  f'Requisição enviada com sucesso!!'
    
    else:
        app.logger.info("bad request !\n")

        return "bad request !"
    
    


if  __name__  ==  '__main__' : 
    app.run()