pessoas = []
listaPrincipal = []
maior = menor = 0


while True:
    pessoas.append(str(input('Digite o nome da pessoa: ')))
    pessoas.append(float(input('Digite o peso da pessoa: ')))
    if len(pessoas) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    listaPrincipal.append(pessoas[:])
    pessoas.clear()
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(listaPrincipal)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for c in listaPrincipal:
    if c[1] == maior:
        print(f'[{c[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}kg. Peso de ', end='')
for c in listaPrincipal:
    if c[1] == menor:
        print(f'[{c[0]}] ', end='')
print()