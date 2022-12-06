#Criando um programa que lê um número e em seguida mostre a sequência Fibonacci a partir dele.


print ('-'*50)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*50)

termos = int(input('Quantos termos você quer mostrar? '))

termo1 = 0
termo2 = 1

print('~'*50)
print(f'{termo1} --> {termo2}', end='')

contador = 3

while contador <= termos:
    termo3 = termo1 + termo2
    print(f' --> {termo3}', end='')
    termo1 = termo2
    termo2 = termo3
    contador += 1
print('-->  FIM!')
print('~'*50)
