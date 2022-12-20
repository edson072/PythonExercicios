#criando uma lista através dos números digitados pelos usuárioe dividindo-a em pares e ímpares.


numeors =  [[], []]

valor = 0

for i in range (1, 8):
    valor = int (input(f'Digite o {i}º valor: '))
    if valor % 2 == 0:
        numeors[0].append(valor)
    else:
        numeors[1].append(valor)

print('-='*30)

numeors[0].sort()
numeors[1].sort()
print(f'Os valores pares digitados foram: {numeors[0]}')
print(f'Os valores ímpares digitados foram: {numeors[1]}')


