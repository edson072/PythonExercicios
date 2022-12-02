num = int(input('Digite um numero: '))
cont = 0

for i in range(1, num + 1):
    if num % i == 0:
        print('\033[31m', end=' ')
        cont += 1
    else:
        print ('\033[31m', end=' ')
    print('{}'.format(i), end=' ')

print('\n\033[mO número {} foi divisível {} vezes'.format(num, cont))
if cont == 2:
    print ('E por isso ele é PRIMO!')
else: 
    print ('E por isso ele NÃO É PRIMO!')
    