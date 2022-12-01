from random import randint
itens = ('PEDRA','PAPEL','TESOURA')
eu = randint (0,2) #"eu" se referete ao computador

print('-=-'*12)
voce = int(input('Digite 0 para PEDRA 1 para PAPEL e 2 para TESOURA  ')) #"voce" se referete ao jogador
print('-=-'*12)

print('Eu joguei {}'.format(itens[eu]))
print('Você jogou {}'.format(itens[voce]))
print('-=-'*12)

if eu == 0: #Computador jogou PEDRA
    if   voce == 0:
        print('O jogo deu EMPATE!')
    elif voce == 1:
        print('Você VENCEU!') #Jogador venceu
    elif voce == 2:
        print('Eu VENCI! Hehe he...') #Computador venceu
    elif voce != 0 or voce != 1 or voce !=2:
        print('Jogada INVÁLIDA! Jogue direito!')
elif eu == 1: #Computador jogou PAPEL
    if   voce == 0:
        print('Eu VENCI! Hehehe...') #Computador venceu
    elif voce == 1:
        print('O jogo deu EMPATE!')
    elif voce == 2:
        print('Você VENCEU!') #Jogador venceu
    elif voce != 0 or voce != 1 or voce !=2:
        print('Jogada INVÁLIDA! Jogue direito!')
elif eu == 2: #Computador jogou TESOURA
    if  voce == 0:
        print('Você VENCEU!') #Jogador venceu
    elif voce == 1:
        print('Eu VENCI! Hehehe...') #Computador venceu
    elif voce == 2:
        print('O jogo deu EMPATE!')
    elif voce != 0 or voce != 1 or voce !=2:
        print('Jogada INVÁLIDA! Jogue direito!')
print('-=-'*12)