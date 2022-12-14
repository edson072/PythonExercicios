numerias = []

while True:
    numerias.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N]' ))
    if resposta in 'Nn':
        break
print ('-='*30)
print(f'Você digitou {len(numerias)} elementos.')
numerias.sort(reverse = True)
print(f'Os valores em ordem decrescente são {numerias}')
if 5 in numerias:
    print('O valor 5 faz parte da lista!')
else: 
    print('O valor 5 não foi encontrado na lista!')
