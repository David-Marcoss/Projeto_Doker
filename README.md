# Projeto_Doker
  Uma aplicação para consulta de endereço utilizando o ceep via api,  a aplicação será distribuida em multiplos containers usando docker, a aplicação é constituida por 5 containers.
 
 - <strong>Container Ator</strong>: Uma aplicação web implementada com flask, por onde o usuario pode enviar seu cep, apartir de uma requisição recebida envia a requisição para o container produtor.

 - <strong>Container Produtor</strong>: Uma aplicação implementada com flask, que recebe requisições do Container Ator e envia para uma fila rabbitmq.

 - <strong>Container rabbitmq</strong>: Container que roda um servidor rabbitmq responsavel por armazenar as mensagens enviadas pelo Container Produtor.

 - <strong>Container Consulmidor</strong>: Container responsavel por receber as mensagens da fila do Container rabbitmq e converter os dados da requisições da fila, acessando uma api externa de endereções que retorna as informações de localização dado um cep, com os novos dados obtidos, os dados são enviados para o container mysql.

 - <strong>Container Mysql</strong>: Container que roda um servidor mysql, responsavel por receber os dados do Container Consulmidor e armazena-los no banco de dados.


## Dependência: 

- python
- docker
- docker compose 

## Rodando Projeto:
    
    docker compose up

## Acessando aplicação:

    http://localhost:8000/
