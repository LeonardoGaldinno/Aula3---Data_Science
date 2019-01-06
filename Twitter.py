import oauth2
import json


class Twitter:
    def __init__(self, consumer_key,consumer_secret,token_key,token_secret):
        self.conexao(consumer_key,consumer_secret,token_key,token_secret)

    def conexao(self, consumer_key,consumer_secret,token_key,token_secret):
        self.consumer = oauth2.Consumer(consumer_key, consumer_secret)
        self.token = oauth2.Token(token_key, token_secret)
        self.cliente = oauth2.Client(self.consumer, self.token)


    def tweet(self, novo_tweet):
        requisicao = self.cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + novo_tweet, method='POST')

        decodificar = requisicao[1].decode()
        objeto = json.loads(decodificar)
        return objeto

    def search(self, pesquisa, lang):
        requisicao = self.cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + pesquisa + '&lang=' + lang)

        decodificar = requisicao[1].decode()
        objeto = json.loads(decodificar)
        twittes = objeto['statuses']


        return twittes
