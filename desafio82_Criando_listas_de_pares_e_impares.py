#Criando uma lista de pares e ímpares com os números digitados.


numeros = []
numerospares = []
numerosimpares = []

while True:
    numeros.append(int(input('Digite um número: ')))
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break
for i, k in enumerate(numeros):
    if k % 2 == 0:
        numerospares.append(k)
    else:
        numerosimpares.append(k)
print('-='*30)
print(f'A lista completa é {numeros} ')
print(f'A lista de pares é {numerospares} ')
print(f'A lista de ímpares é {numerosimpares}')
