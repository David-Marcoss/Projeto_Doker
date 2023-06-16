import requests

cep = '04601671'

req = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

endereco = req.json()

if endereco != {'erro': True}:
    print(endereco["cep"],endereco["logradouro"],endereco["bairro"],endereco["uf"])