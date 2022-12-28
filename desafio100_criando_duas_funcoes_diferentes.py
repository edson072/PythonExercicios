#criando um programa que cria duas funções, uma para sortear uma lista de números e outra para somar apenas os números pares digitados.


from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for contador in range (0,5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

números = []
sorteia(números)
somaPar(números)