nome     = input('Digite o nome do aluno')
nota1    = int(input('Digite a primeira nota do aluno {}'.format(nome)))
nota2    = int(input('Digite a segunda nota do aluno {}'.format(nome)))
media    = (nota1 + nota2) / 2
print('A média das notas do aluno {} é de {}.'.format((nome),(media)))