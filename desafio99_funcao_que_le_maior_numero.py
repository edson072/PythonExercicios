#criando uma função que lê vários números da função de um parâmetro e retorne quem é o maior deles.

from time import sleep

def maior (* num):
    contador = maior = 0
    print('Analisando os valores passados... ')
    for valor in num:
        print (f'{valor} ', end='', flush=True)
        sleep(0.3)
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1
    print(f'Foram informados {contador} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1,2)
maior(6)
maior()