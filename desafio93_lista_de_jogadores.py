#Criando um programa que armazena em um dicionário a quantidade de partidas disputadas por um jogador e a quantidade de gols marcados por ele.


jogador = dict()
jogos = list()

jogador['nome'] = str(input('Digite o nome do jogador: '))
total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range (0, total):
    jogos.append(int(input(f'Quantos gols {jogador ["nome"]} fez na {c + 1}ª partida? ')))
jogador['gols'] = jogos[:]
jogador['total'] = sum(jogos)

print("-=" * 30)
print(jogador)
print('-=' * 30)

for k, v in jogador. items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')

for i, v in enumerate(jogador ['gols']):
    print(f'  => Na {i + 1}ª partida ele fez {v} gols')
print(f'{jogador ["nome"]} fez um total de {jogador ["total"]} gols')