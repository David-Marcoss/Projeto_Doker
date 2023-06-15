import requests

cep = '64601671'

req = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

endereco = req.json()


print(endereco["cep"],endereco["logradouro"],endereco["bairro"],endereco["uf"])