from typing import Dict
import pika
import json

class RabbitmqPublisher:
    def __init__(self) -> None:
        self.__host = "172.19.0.2"
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__queue = "My_fila"
        self.__exchange = "My_exchange"
        self.__routing_key = ""
        self.__channel = self.__create_channel()
        self.__create_exchange()
        self.__create_bind()

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
        
        return channel

    def __create_exchange(self):
        self.__channel.exchange_declare(
            exchange=self.__exchange,
            exchange_type='direct',
            passive=False,
            durable=True,
            auto_delete=False
        )
        self.__channel.queue_declare(queue=self.__queue, durable=True)
    
    def __create_bind(self):
        self.__channel.queue_bind(
            queue=self.__queue,
            exchange=self.__exchange,
            routing_key=""
        )

    def send_message(self, body: Dict):
        self.__channel.basic_publish(
            exchange=self.__exchange,
            routing_key=self.__routing_key,
            body=json.dumps(body),
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )
