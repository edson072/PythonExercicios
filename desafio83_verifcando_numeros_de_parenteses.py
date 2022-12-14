#criando um programa que verifica se o número de parênteses de uma determinada função está correto.



funcao = str(input('Digite uma função que contenha paranteses: '))
pilhaParenteses = []

for simbolo in funcao:
    if simbolo == '(':
        pilhaParenteses.append('(')
    elif simbolo == ')':
        if len(pilhaParenteses) > 0:
            pilhaParenteses.pop()
        else:
            pilhaParenteses.append(')')
            break
if len(pilhaParenteses) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')


