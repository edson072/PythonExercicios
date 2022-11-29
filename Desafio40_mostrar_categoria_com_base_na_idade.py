idade = int(input('Digite a idade do atleta: '))

if idade < 9:
    print('A categoria do atleta é MIRIM')
elif idade >=9 and idade < 14:
    print('A categoria do atleta é INFANTIL')
elif idade >=14 and idade < 19:
    print('A categoria do atleta é JUNIOR')
elif idade >=19 and idade <20:
    print ('A categoria do atleta é SÊMIOR.')
else:
    print ('A categoria do atleta é MASTER.')
    