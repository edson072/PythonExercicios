from random import randint
from time import sleep
computador = randint(0,5) # Isso faz o computador "pensar"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer! Eu pensei no número {}'.format(computador))
else:
    print('GANHEI! Eu pensei no número {}!'.format(computador, jogador))