#Criando um programa que simula um caixa eletrônico, que contém cédulas de R$50,00 R$20,00 R$10,00 e R$1,00



print('='*30)
print('{:^30}'.format('BANCO VOCÊ MAIS RICO'))
print('='*30)

saque = int(input('Que valor você quer sacar? R$ '))
totalSaque = saque

cedula = 50
totalCedula = 0

while True:
    if totalSaque >= cedula:
        totalSaque -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'total de {totalCedula} cédulas de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedula = 0
        if totalSaque == 0:
            break
print('='*30)
print('volte sempre so BANCO CEV! Tenha um bom dia!')