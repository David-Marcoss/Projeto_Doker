from src.config.fila_connection import RabbitmqConsumer
import requests
from src import enderecos_op

#função responsavel por receber msg da fila e processa-la
def minha_callback(ch, method, properties, body):

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


if  __name__  ==  '__main__' :

    rabitmq_consumer = RabbitmqConsumer(minha_callback)
    rabitmq_consumer.start()