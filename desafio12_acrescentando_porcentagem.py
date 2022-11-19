preco       = float(input('Digite o preço do produto R$:'))
novoPreco   = preco - (preco * 0.05)

print('O preço é R$ {:.2f} e com o desconto de 5% fica R$ {:.2f}'.format(preco, novoPreco))