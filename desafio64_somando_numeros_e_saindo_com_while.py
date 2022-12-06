#Criando um programa que soma todos os números digitados pelo usuário até que ele digite o número "999" para sair.


num = contador = soma = 0
num = int(input('Digite um número [999 para parar]: '))

while num != 999:
    soma += num
    contador += 1
    num = int(input('Digite um número [999 para parar]: '))

print (f'Você digitou {contador} números e a soma entre eles foi {soma}.')