#Criando uma tabuada utilizando o laço "for in"

num = int(input('Digite o número do qual quer saber a tabuada: '))

for i in range (1, 11):
    print ('{} x {:2} = {}'.format(num, i, num*i))