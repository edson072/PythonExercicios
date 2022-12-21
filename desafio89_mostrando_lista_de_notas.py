#Criando um programa que elabora a lista completa de alunos com suas respectivas médias.

boletin = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    boletin.append([nome, [nota1, nota2], media])
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break

print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'* 35)
for i, a in enumerate(boletin):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.12f}')
while True:
    print('-' * 35)
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): ' ))
    if opcao == 999:
        print('FINALIZANDO...')
        break
    if opcao <= len (boletin) - 1:
        print(f'Notas de {boletin[opcao[0]]} são {boletin[opcao[[1]]]}')
print('<<< VOLTE SEMPRE >>>>')
