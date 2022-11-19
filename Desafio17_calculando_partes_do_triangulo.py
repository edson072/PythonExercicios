from math import hypot
cateto      = float(input('Compriimento do cateto aposto: '))
catetoAd    = float(input('Comprimento do cateto adjacente: '))
hipotenusa  = hypot(cateto,catetoAd)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))