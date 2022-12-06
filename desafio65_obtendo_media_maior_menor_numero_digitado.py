#Criando um programa que soma todos os números digitados pelo usuário, retorne a soma, a média, o menor e o maior entre eles.


resposta = 'S'
somador = quantidade = media = maiorNum = menorNum = 0

while resposta in 'Ss':
    num = int(input('Digite um número: '))
    somador += num
    quantidade += 1
    if quantidade == 1:
        maiorNum = menorNum = num
    else:
        if num > maiorNum:
            maiorNum = num
        if num < menorNum:
            menorNum = num
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

media = somador / quantidade
print(f'Você digitou {quantidade} números e a média foi {media}')
print(f'O maior valor foi {maiorNum} e o menor foi {menorNum}.')