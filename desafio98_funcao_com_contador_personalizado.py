#criando um programa com uma função com um contador personalizado.


from time import sleep

def contador (a, b, c):
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    print('-=' * 20)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    sleep(2.5)

    if a < b: 
        contador = a
        while contador <= b:
            print(f'{contador} ', end='', flush=True)
            sleep(0.5)
            contador += c
        print('FIM!')
    else:
        contador = a
        while contador >= b:
            print(f'{contador} ', end='', flush=True)
            sleep(0.5)
            contador -= c
            print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Digite o número inícial: '))
fim = int(input('Digite o número final: '))
passo = int(input('Digite o número em que a contagem se dará: '))
contador(inicio, fim, passo)