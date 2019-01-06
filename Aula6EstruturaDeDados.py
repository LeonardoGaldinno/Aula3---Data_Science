minha_lista=['Leonardo','Joao'] #List / ordenada / Possui itens
minha_tupla=('Leonardo','Joao') #Tuple /imutavel
meu_dicionario={'Nome':'Leonardo','Idade':21} #Dicionario / possui chave e significado / chave e registro / nao ordenado
meu_conjunto={'Leo','Joao'} #Conjunto / nao possui dados repetidos / busca rapida

'''
if 'Leonardo' in minha_tupla:
    print(minha_tupla)
'''
'''
print(meu_dicionario['Nome'])
print(len(meu_dicionario)) #Len pode ser usado em qualquer colecao
'''
'''
if 'Leonardo' in meu_dicionario.values():
    print('Leonardo esta no dicionario')
'''
'''
for valores in meu_dicionario.keys():
    print(valores)
'''
'''
meu_dicionario['Nome'] = 'Leo'
meu_dicionario['Sobrenome'] = 'Galdino'
print(meu_dicionario)
'''
'''
meu_conjunto.add('Eduardo')
meu_conjunto.remove('Leo')
print(meu_conjunto)
'''
lista = []
tupla = ()
dicionario = {}
conjunto = set()

