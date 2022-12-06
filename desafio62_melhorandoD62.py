#Melhorando o desafio 61, perguntando ao usuário se ele quer mostrar mais termos e encerrando o programa quando ele digitar o zero.


print ('Gerador de PA')
print ('-=-'*10)

primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão da PA: '))
termo = primeiro

contadora = 1
soma = 0
outros = 10

while outros != 0:
    soma = soma + outros
    while contadora <= soma:
        print (f'{termo} -> ',end='')
        termo += razão
        contadora += 1
    print ('PAUSA')
    outros = int(input('Quantos termos você quer mostrar a mais? '))

print (f'Porgressão finalizada com  {soma} termos mostrados.')