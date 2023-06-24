import pika
import requests
import os
from src import enderecos_op




#classe responsavel por fazer conexão com fila , recebe callback
#que é a função responsavel por consulmir mensages da fila
class RabbitmqConsumer:
    def __init__(self) -> None:
        self.__host = '172.19.0.2'
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__queue = 'My_fila'
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
        
        print("-------"*10)
        print(f"Requisição: {body}")

        cep = str(body, 'utf-8')

        cep = cep[1:-1].replace("-",'')

        print(cep)
        
        #fazendo conexão com api externa
        req = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

        if req:
            endereco = req.json()

            if endereco != {'erro': True}:
                #inserindo os dados obtidos via api no bd
                op = enderecos_op()
                op.insert(endereco["cep"],endereco["logradouro"],endereco["bairro"],endereco['localidade'],endereco["uf"])

                print(f"Operação concluida !!\n")

                return True
                
            else:
                print("Cep não encontrado!\n")
                
                return False
        else:
            print("Entrada invalida\n")
                
            return False
            
            
    def start(self):
        print(f'Listen RabbitMQ on Port 5672')
        self.__channel.start_consuming()
