largura = int(input('Digite o número relativo à largura da parde:'))
altura  = int(input('Digite o número relativo à altura da parede'))
area    = largura * altura
tinta   = area / 2

print('A parede tem {} metros de largura e {} metros de altura, totalizando uma área de {}m². A quantidade necessária de tinta para pintá-la são de {} litros'.format((largura),(altura),(area),(tinta)))