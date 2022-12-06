#Criando um gerador de PA utilizando o While


primeiro = int(input('Digite o primeiro númeroo da PA '))

razão = int(input('Digite o número da Razão: '))

termo = primeiro

cont = 1

while cont <= 10:
    print (termo, ' ', end='')
    termo += razão
    cont += 1

print('\n' 'ACABOU!')