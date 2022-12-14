#criando um programa que lê os números digitados pelo usuário e acescente na lista apenas aqueles que não foram ainda inseridos nela.



numeros  = []
while True: 
    i = int(input('Digite um valor: '))
    if i not in numeros:
        numeros.append(i)
        print('Valor adcionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    z = str(input('Quer continuar? [S/N] '))
    if z in 'Nn':
        break
print("-="*30)
numeros.sort()
print(f'Você digitou os valores {numeros}') 