import re
import requests

try:
    requisicao = requests.get('https://www.empiricus.com.br/contato')
    variavel = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', requisicao.text)
    print(variavel)

except Exception as error:
    print('Erro: ', error)

