#criando um programa que lê quatro números digitados pelo teclado e guarde-os em uma tupla e no final mostre quantas vezes apareceu o número 96
#  e em que posição foi digitado o número 3.

num = (int(input('Digite um número: ')), 
        int(input('digite outro número: ')),
        int(input('Dgite mais um número: ')),
        int(input('Digite o último número: ')))

print(f'Você digitou os valores {num}' )
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for i in num:
    if i % 2 == 0:
        print(i, end=' ')