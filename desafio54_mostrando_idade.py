#Criando um programa que lê o nascimento de sete pessoas e diga quantas delas são maiores e quantas são menores.

from datetime import date 
atual = date.today().year

totalMaior = 0
totalMenor = 0

for i in range (1, 8):
    anoNasc = int(input('Digite o ano em que a {}º pessoa nasceu: '.format(i)))
    idade = atual - anoNasc

    if idade >= 18:
        totalMaior += 1
    else:
        totalMenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totalMaior))
print('E também tivemos {} pessoas menores de idade'.format(totalMenor))