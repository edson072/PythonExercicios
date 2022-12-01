#Desenvolvendo um programa que lê um termo e calcula a razao de uma Progressao Aritimética nos 10 primeiros termos.


primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10-1)*razão

for i in range (primeiro, décimo + razão, razão):
    print('{}'.format(i), end= ' -> ')
print('ACABOU!')