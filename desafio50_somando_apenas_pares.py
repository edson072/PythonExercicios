#Desenvolvendo um programa que lê seis numeros inteiros e faça a soma apenas daqueles que são pares.

soma = 0
cont = 0

for i in range (1,7):
    num = int(input('Digite o {}º valor: '.format(i)))
    if num % 2 == 0:
        soma += num
        cont += 1

print('Você informou {} números PARES e a soma foi {}'. format(cont, soma))