#Criando uma tabuada de vários números digitados pelo usuário e que só será interrompido com a digitação de um número negativo pelo usuário.


while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if num < 0:
        break
    for i in range (1, 11):
        print (f'{num} x {i} = {num*i}')
    print('-'*30)
print ('PROGRAMA TABUADA ENCERRADO. Volte sempre!')