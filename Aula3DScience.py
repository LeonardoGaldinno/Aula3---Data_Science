'''
var_verdade = True  # type: bool
var_falso = False

if(var_verdade==False): # No Python 3 funciona sem o parenteses
    print(type(var_verdade))
else:
    print(var_verdade)

____________________________________________________________________________________________________________________
print('1 - Escreva Leonardo\n 2 - Escreva Joao')
opcao = input('Selecione uma opcao: ')

if(opcao == 1):
    print('Voce selecionou a opcao: {}'.format(opcao),'Que escreve Leonardo')
elif(opcao == 2):
    print('Voce selecionou a opcao: {}'.format(opcao),'Que escreve Joao')
else:
    print('Opcao invalida')
'''
idade = input('Digite sua idade: ')
peso = input('Digite o seu peso: ')
altura = input('Digite sua altura: ')

if((idade>18) and (peso>=60) and (altura>=1.70)):
    print('Parabens, voce esta apto para servir o exercito !')
else:
    print('Voce nao esta apto para servir')