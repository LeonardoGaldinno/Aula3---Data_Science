import requests
'''''
try:
    requisicao = requests.get('https://g1.com.br')
    #print (requisicao.status_code)
    print(requisicao.text)

except Exception as erro:
    print('Ocorreu um erro: ',erro)
'''

cabecalho = {'user-agent':'Windows 7',
             'Referer':'https://www.google.com'}

meus_cookies = {'Ultima visita':'28.06.2015'}

dados = {'username':'user',
         'password':'password'}

try:
    requisicao = requests.post('https://www.google.com',
                           headers=cabecalho,
                           cookies=meus_cookies,
                           data=dados)
except Exception as erro:
    print('Ocorreu um erro: ', erro)