#Criando um programa que lê o aproveitamento dos jogadores de futebol com base nas respectivas atuações.



clube = []
atleta = dict()
jogos = []

while True:
    atleta.clear()
    atleta['nome'] = str(input('Digite o nome do jogador: '))
    total = int(input(f'Quantas partidas {atleta["nome"]} jogou?  '))
    jogos.clear()
    
    for c in range(0, total):
        jogos.append((int(input(f'Quantos gols {atleta["nome"]} marcou na {c+1}ª partida?  '))))
    atleta ['gols'] = jogos[:]
    atleta['total'] = sum(jogos)
    clube.append(atleta.copy())

    while True:
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in atleta.keys():
    print(f'{i<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(clube):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(clube):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f'-- LEVANTAMENTO  DO JOGADOR {clube[busca]}:')
        for i, g in enumerate(clube[busca]['gols']):
            print(f'No {i+1}º jogo {atleta["nome"]} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>>')
    