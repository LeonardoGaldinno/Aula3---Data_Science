from Twitter import Twitter
import pprint

consumer_key = 'xrY6V4Ues00o9jr5mdLlto6uJ'
consumer_secret = 'oscjnGiRUOrQM6wrxLwOoBZ2dvmBN9FJjkTmGZHaXViYlla6EM'

token_key = '307586034-sP38XqIK6d2PhNosXXBLfbNvUWUIywMCRm2g8R9v'
token_secret = 'BbIwJPXN7rGEmQDc2f5Ufueo76lDChlJ6INrLgc9g1Fxy'


twitter = Twitter(consumer_key,consumer_secret,token_key,token_secret)
try:

    pesquisa = Twitter.search(twitter,'globo','pt')
    #pprint.pprint(pesquisa)
    for resultado in pesquisa:
        pprint.pprint('User: ' + resultado['user']['screen_name'])
        print()
        pprint.pprint('Tweet: '+ resultado['text'])



except Exception as Error:
    print('Houve um erro: ', Error)


'''
try:
    resp = twitter.tweet('PostIt')

except Exception as Error:
    print('Houve um erro: ', Error)
'''



