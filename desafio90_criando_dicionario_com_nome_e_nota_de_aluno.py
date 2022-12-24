#criando um programa que gera um dicinário com dados de todos os alunos cadastrados no respectivo sistema.



aluno = dict()
aluno ['nome'] = str(input('Nome: '))
aluno['média '] = float(input(f'Média de {aluno["nome"]}: '))

if aluno ['média '] >= 7:
    aluno ['situação'] = 'Aprovado'
elif 5 <= aluno ['média '] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno ['situação'] = 'Reprovado'
print('-='*30)

for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')