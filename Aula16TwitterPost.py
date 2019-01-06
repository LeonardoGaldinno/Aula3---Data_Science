import oauth2
import json
import pprint
#import urllib.parse


consumer_key = 'xrY6V4Ues00o9jr5mdLlto6uJ'
consumer_secret = 'oscjnGiRUOrQM6wrxLwOoBZ2dvmBN9FJjkTmGZHaXViYlla6EM'

token_key = '307586034-sP38XqIK6d2PhNosXXBLfbNvUWUIywMCRm2g8R9v'
token_secret = 'BbIwJPXN7rGEmQDc2f5Ufueo76lDChlJ6INrLgc9g1Fxy'

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)



cliente = oauth2.Client(consumer, token)
novo = input('Novo Tweet: ')
#pesquisa_codificada = urllib.parse.quote(pesquisa, safe='')
requisicao = cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + novo, method = 'POST')
#requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + pesquisa_codificada + '&lang=pt')

#print(type(requisicao[0]))
#print(type(requisicao[1]))

decodificar = requisicao[1].decode()
#print(type(decodificar))
objeto = json.loads(decodificar)
print(objeto)

'''
pprint.pprint(objeto['statuses'][0]['user']['screen_name'])
pprint.pprint(objeto['statuses'][0]['text'])

twittes = objeto['statuses']

for tweet in twittes:
    print(tweet['user']['screen_name'])
    print(tweet['text'])
    print()

'''