#Criando um programa que lê a classificação dos times no brasileirão, bem como determine quem são os 5 primeiros, os 4 ultimos e onde se encontra o Corinthians.


times = ('Plameiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Atlético PR', 'Atlético Mineiro', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-Goianiese', 'Avaí', 'Juventude' )

print("="*80)
print(f'Os 5 primeiros colocados do Brasileirão são: {times[0:5]}')
print("="*80)
print(f'Os 4 ultimos colocados do Brasileirão são: {times[-4:]} ')
print("="*80)
print(f'Os times do Brasileirão em ordem alfabética ficam assim: {sorted(times)}')
print("="*80)
print(f'O Corinthians se encontra na {times.index("Corinthians")}ª posição do Brasileirão.')