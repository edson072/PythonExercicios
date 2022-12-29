#criando uma função que elabora uma ficha com o nome dos jogadores e a mostre com os nomes e os respectivos dados de cada jogador.


def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


#Programa principal
nomeJogador = str(input("Nome do jogador: "))
gols = str(input("Número de Gols: "))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nomeJogador.strip() == '':
    ficha(gol=gols)
else: ficha(nomeJogador, gols)