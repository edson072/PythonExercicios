reta1 = float(input('Digite o tamanho do primeiro segmento: '))
reta2 = float(input('Digite o tamanho do segundo segmento: '))
reta3 = float(input('Digite o tamanho do terceiro segmento: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os segmentos acima PODEM formar um triâgulo')
    if reta1 == reta2 == reta3:
        print('EQUILÁTERO')
    elif reta1 != reta2 != reta3 != reta1:
        print('ESCALENO!')
    else:
        print('ISÓCELES')
else:
    print('Os segmentos acima NÃO PODEM forma um triângulo')