import requests

zip = ''

request = requests.get('https://viacep.com.br/ws/%s/json/' %(zip))

address  = request.json()

print(address['localidade'])