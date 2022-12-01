preco           = float(input('Qual é o valor do produto? '))
formaPagamento  = int(input('Digite 1 para pagamento À VISTA ou no CHEQUE; 2 para pagamento À VISTA NO CARTÃO; 3 para pagamento A PRAZO NO CARTÃO em até 2 vezes; e 4 para pagamento A PRAZO NO CARTÃO em até 3 vezes ou mais '))

avista          = preco - (preco * 10 / 100)
avistaCartao    = preco - (preco * 5 / 100)
cartao3vezes    = preco + (preco * 20 / 100)

if formaPagamento == 1:
    print('Você pagará R$ {:.2f} com o desconto.'.format(avista))
elif formaPagamento == 2:
    print('Você pagará R$ {:.2f} com o desconto.'.format(avistaCartao))
elif formaPagamento == 3:
    print('Você não terá desconto no preço do produto e deverá pagar {:.2f}.'.format(preco))
elif formaPagamento ==4:
    print('Você deverá pagar o valor do produto com um acréscimo de R${:.2f} referente aos juros. O valor total será de R${:.2f}.'.format(cartao3vezes - preco, cartao3vezes))