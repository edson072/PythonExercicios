
from time import sleep

primeiroNum = int(input('Digite o primeiro valor: '))
segundoNum = int(input('Digite o segundo valor: '))

opção = 0

while opção != 5:
    print (''' [ 1 ] somar  [ 2 ] multiplicar [ 3 ] maior  [ 4 ] novos números  [ 5 ] sair do programa ''')

    opção = int(input(' >>>>>> Qual é sua opção? '))
    if opção == 1:
        soma = primeiroNum + segundoNum
        print('A soma entre {} + {} é {}'. format(primeiroNum, segundoNum, soma))
    elif opção == 2:
        produto = primeiroNum * segundoNum
        print('O resultado de {} x {} é {}'. format(primeiroNum, segundoNum, produto))
    elif opção == 3:
        if primeiroNum > segundoNum:
                maior = primeiroNum
        else:
                maior = segundoNum
        print('Entre {} e {} o maior valor é {}'.format(primeiroNum, segundoNum, maior))
    elif opção == 4:
        print('Informe os números novamente: ')
        primeiroNum = int(input('Digite o primeiro valor: '))
        segundoNum = int(input('Digite o segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
        sleep(1.5)
    else:
        print('Opção inválida tente novamente')
    print('=-='*10)
print('Fim do programa! Volte sempre!')
            
