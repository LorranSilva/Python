import requests

cep = input('digite o cep: ')
url = ('http://www.viacep.com.br/ws/%s/json' %cep)
zip = requests.get(url)

resultado = zip.json()

print(resultado)