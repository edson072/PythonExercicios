num = int(input('Digite um número para calcular seu fatorial: '))
cont = num
fator = 1

print('Calculando {} = ' .format(num), end='')
while cont > 0:
    print(cont, end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fator *= cont
    cont -= 1

print(fator)


