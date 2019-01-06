lista_nomes = ['Leo', 'Caio','Lucas']
lista_nomes.append('Joao')
lista_nomes.append('Eduardo')
lista_nomes.insert(1,'Leonardo')
lista_nomes[0] = 'Nome'
lista_nomes.insert(3, 'Nathalia')
lista_nomes.remove('Caio')
lista_nomes.remove('Lucas')
lista_nomes.remove('Joao')
lista_nomes.remove('Eduardo')
lista_nomes.remove('Nome')
print(lista_nomes.pop(0) + ':')
frase1 = 'Oi, tudo bem, podemos falar, agora, por favor'
frase = ' Eu te amo'
if(lista_nomes[0] == 'Nathalia'):
    print(lista_nomes[0] + frase + ' de mais')
    print(len(lista_nomes))
    print frase1.split(',')
    print(len(frase1))
    print(frase1[0:45])
else:
    print('else')
