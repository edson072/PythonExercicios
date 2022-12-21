#Criando um programa que gera uma lista de seis números a serem sorteados de 1 a 60.

from random import randint
from time import sleep
lista = list()
jogos = list()
print('-'*30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))

total = 1
while total <= quant:
    cont = 0
    while True:
        num = randint (1,60) 
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total +=1
print('-='*3, f'SORTEANDO {quant} JOGOS ', '-='*3)
for i, l in enumerate(jogos):
    print (f'jogo {i+1}: {l}')
    sleep(1)
print('-='* 5, '< BOA SORTE! >', '-=' * 5)

