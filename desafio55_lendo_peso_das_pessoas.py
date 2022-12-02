#Criando um programa que lê o peso de 5 pessoas e depois mostre quais foram o menor e o maior peso.

maiorPeso = 0
menorPeso = 0

for i in range (1, 6):
    peso = int(input('Digite o peso da {}º pessoa: '.format(i)))
    if i == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso

print('O maior peso lido foi de {}Kg'.format(maiorPeso))
print('O menor peso lido foi de {}kg'.format(menorPeso))


