    #Criando um leitor de boletins de notas através de uma biblioteca que vai receber os dados dos usuários alunos.

def notas(*n, sit=False):
    """
    --> Função para analisar notas e situações de vários alunos.
    :parêmetro n: uma ou mais notas dos alunos (aceita várias)
    :parêmetro sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)

    if sit:
        if r['média'] >=7:
            r['situação'] = 'BOA'
        elif r ['média'] >= 5:
            r['situação'] =  'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

# Programa Principal
respota = notas (5.5, 2.5, 1.5, sit=True)
print(respota)
help(notas)