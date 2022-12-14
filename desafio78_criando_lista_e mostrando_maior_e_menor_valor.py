#Criando um programa que lê cinco números e diga ao o maior, o menor e suas respectivas posições.



numeros = []
maior = []
menor = []

for i in range (0,5):
    numeros.append(int(input(f'Digite um valor para a Posição {i}: ')))
    if i == 0:
        maior = menor = numeros[i]
    else:
        if numeros[i] > maior:
            maior = numeros[i]
        if numeros[i] < menor:
            menor = numeros[i]
print('='*30)
print(f'Você digitou os valores {numeros}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, t in enumerate(numeros):
    if t == maior:
        print(f'{i}... ', end='')
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, t in enumerate(numeros):
    if t == menor:
        print(f'{i}... ', end='')
print()
