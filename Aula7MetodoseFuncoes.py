numero = input('Informe quantos numeros tera sua colecao: ')

repeticao = 0
lista=[]
variavel = []

while repeticao < numero:
    informe = input('Informe o numero: ')
    lista.append(informe)
    repeticao += 1

def maior_numero():
    maior = max(lista)
    return maior

variavel = maior_numero()
print(variavel)





