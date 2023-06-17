import pika
import requests

from src import enderecos_op




#classe responsavel por fazer conexão com fila , recebe callback
#que é a função responsavel por consulmir mensages da fila
class RabbitmqConsumer:
    def __init__(self) -> None:
        self.__host = "localhost"
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__queue = "My_fila"
        self.__channel = self.__create_channel()

    #cria conexão com a flia
    def __create_channel(self):
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(
                username=self.__username,
                password=self.__password
            )
        )

        channel = pika.BlockingConnection(connection_parameters).channel()
        channel.queue_declare(
            queue=self.__queue,
            durable=True
        )
        channel.basic_consume(
            queue=self.__queue,
            auto_ack=True,
            on_message_callback=self.__callback
        )

        return channel

    
    #função responsavel por receber msg da fila e processa-la
    def __callback(self,ch, method, properties, body):

        cep = str(body, 'utf-8')

        
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
        
    def start(self):
        print(f'Listen RabbitMQ on Port 5672')
        self.__channel.start_consuming()
