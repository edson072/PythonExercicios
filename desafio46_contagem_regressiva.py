#Criando um programa que mostre na tela a contagem regressiva, para o Ano novo, iniciando em 10 com intervalo de 1 segundo entre cada contagem.

from time import sleep

for i in range (10, -1, -1):
    print(i)
    sleep(1)
print('FELIZ ANO NOVOOOO!!! BUM! BUM! POOOOOOW!') 