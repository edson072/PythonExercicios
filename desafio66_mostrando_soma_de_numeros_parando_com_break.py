#Criando um programa que soma todos os números digitados pelo usuário até que ele digite o número "999". A parada se udar utilizando o método "break".


contador = 0 
soma = 0


while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    soma += num
    contador += 1
    

print (f'Você digitou {contador} números e a soma entre eles foi {soma}.')