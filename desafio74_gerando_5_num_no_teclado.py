#Criando um programa que lê cinco números alatórios e colocá-los em uma tupla. Depois mostre a listagem dos números indicando qual o maior e o menor número na tupla.

from random import randint

numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print(f'Os valores sorteados foram: ', end= ' ' )
for i in numeros:
    print(f'{i} ', end='')
print(f'\n O maior valor sorteado foi {max(numeros)} ')
print(f'O menor valor sorteado foi {min(numeros)}')
