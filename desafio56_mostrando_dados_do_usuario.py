#Criando um programa que lê os dados pessoais de 4 pessoas e mostre a média de idade delas; qual o homem mais velho entre eles; e quantas mulheres tem abaixo de 20 anos.

somaIdade = 0
mediaIdade = 0
maiorHomem = 0
nomeVelho = ''
totalMulher20 = 0

for i in range (1, 5):
        
        print('--------------{}ª PESSOA-----------'.format(i))
        nome = str(input('Nome: ')).strip()
        idade = int(input('Idade: '))
        sexo = str(input('Sexo[M/F]: ')).strip()
        somaIdade += idade

        if i ==1 and sexo in 'Mm':
            maiorHomem = idade
            nomeVelho = nome
        if sexo in 'Mm'and idade > maiorHomem:
            maiorHomem = idade
            nomeVelho = nome
        if sexo in 'Ff' and idade < 20:
            totalMulher20 += 1
        mediaIdade = somaIdade / 4

print ('A média de idade do grupo é de {} anos'. format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorHomem, nomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totalMulher20))