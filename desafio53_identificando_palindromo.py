frase = str (input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)

inverso = ''

for i in range (len (junto) -1, -1, -1):
    inverso += junto[i]
if inverso == junto:
    print ('Temos um palíndromo!')
else:
    print ('A frase digitada não é um palíndromo!')