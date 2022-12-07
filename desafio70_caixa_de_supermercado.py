#criando um programa que lê o preço dos produtos digitados, diz qual é o gasto total da compra, quantos produtos custaram mais de 1000 e qual é o produto mais barato.



total = totalMil = menor = contador = 0
barato = ''

while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preco: R$ '))
    contador += 1
    total += preço

    if preço > 1000:
        totalMil += 1
    if contador == 1 or preço < menor:
        menor = preço
        barato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]' )).strip().upper()[0]
    if resposta == 'N':
        break

print('{:~^40}'.format('FIM DO PROGRAMA '))
print(f'O total da compra foi R$ {total:.2f}')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')