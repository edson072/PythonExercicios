#Criando um Jogo Par ou Ímpar

from random import randint

vezes = 0

while True:
    usuario = int (input ('Diga um valor: '))
    computador = randint (0, 10)
    total = usuario + computador
    modelo = ' '

    while modelo not in 'PI':
        modelo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {usuario} e eu joguei {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')

    if modelo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vezes += 1
        else:
            print('Você PERDEU!')
            break
    elif modelo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vezes += 1
        else:
            print('Você PERDEU!')
            break
    print ('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vezes} vezes.')