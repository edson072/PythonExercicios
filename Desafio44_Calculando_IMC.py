altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))

IMC = peso / (altura **2)

if IMC < 18.5:
    print('Seu IMC é {:.1f} você está abaixo do peso.'.format(IMC))
elif IMC >=18.5 and IMC < 25:
    print('Seu IMC é {:.1f} você está no peso ideal'.format(IMC))
elif IMC >=25 and IMC < 30:
    print('Seu IMC é {:.1f} você está com sobrepeso.'.format(IMC))
elif IMC >=30 and IMC < 40:
    print('Seu IMC é {:.1f} você está com obsidade'.format(IMC))
else:
    print('Seu IMC é {:.1f} você está com obsidade mórbida.'.format(IMC))