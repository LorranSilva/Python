import requests
# import xml.etree.ElementTree as ET
import xmltodict

requisicao = requests.get('https://viacep.com.br/ws/01001000/xml/')
print(requisicao.content)

# usando a raiz da estrutura para criar um dicionario
# root = ET.fromstring(requisicao.content)

# acessando dados com 'iter', para visualizar tudo '*' (curinga)
# for child in root.iter('*'):
#     print(child.tag)

my_dict = xmltodict.parse(requisicao.content)
print(my_dict)