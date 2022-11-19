salario     = int(input('Digite o valor relativo ao salário: R$ '))
novoSal     = salario + (salario * 15 / 100)

print('O salário atual é de R${:.2f} e novo salário, com 15% de aumento, é de R${:.2f}'.format(salario,novoSal))