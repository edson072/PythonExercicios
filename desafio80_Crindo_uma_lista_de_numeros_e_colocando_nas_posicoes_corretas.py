listaNumeros = []

for i in range (0, 5):
    numero = int(input('Digite um valor: '))
    if i == 0 or numero > listaNumeros [-1]:
        listaNumeros.append(numero)
        print('Adcionado ao final da lista...')
    else:
        posterior = 0
        while posterior < len(listaNumeros):
            if numero <= listaNumeros[posterior]:
                listaNumeros.insert(posterior, numero)
                print (f'Adicionado na posição {posterior} da lista...')
                break
            posterior +=1
print('-='*30)
print(f'Os valores digitados em ordem foram {listaNumeros}')