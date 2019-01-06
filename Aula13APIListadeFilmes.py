import requests
import json
'''
def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?t='+titulo+'&type=movie'+'&apikey=8cfc684c')
        dicionario = json.loads(req.text)
        return dicionario

    except Exception as erro:
        print('Ocorreu um erro: ', erro)
        exit()
        
def printar_detalhes(filme):
    print('Titulo: {}'.format(filme['Title']))
    print('Ano: {} '.format(filme['Year']))
    print('Diretor: {} '.format(filme['Director']))
    print('Atores: {} \n'.format(filme['Actors']))


sair = False

while not sair:
    op = input('Digite o nome do filme ou sair para sair do programa: ')
    if op == 'SAIR':
        sair = True
        print('Saindo...')
        exit()

    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print('Filme nao encontrado ')
        else:
            printar_detalhes(filme)
'''

def requisicao (titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?s='+titulo+'&page=2'+'&apikey=8cfc684c')
        dicionario = json.loads(req.text)
        return dicionario

    except Exception as error:
        print('Ocorreu um erro: ', error)

def printar_filme(filme):
    print('Pesquisa: {}'.format(filme['Search']))

sair = False
while not sair:
    op=input('Digite o nome de um filme ou SAIR para sair do programa: ')
    if op == 'SAIR':
        print('Saindo...')
        exit()
    else:
        filme = requisicao(op)
        printar_filme(filme)













