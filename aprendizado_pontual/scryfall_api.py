import requests

def busca_nome(word, resultado):
    if word not in resultado:
        return False
    else:
        print(resultado.title())
        return True

#  buscando o nome do card
card_name = 'abble' # input('Nome da carta: ')

url = 'https://api.scryfall.com/cards/search'
params = {'q': card_name}
 
a = requests.get(url, params=params)
resultado = a.json()

for k in resultado['data']:
    print(f'{k}\n')