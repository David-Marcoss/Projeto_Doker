import sys
from src.config.fila_connection import RabbitmqConsumer
from time import sleep

print("_________________________"*10, file=sys.stderr)
print("Conectando com a fila Rabbitmq ....", file=sys.stderr)


sleep(20)
rabitmq_consumer = RabbitmqConsumer()
rabitmq_consumer.start()