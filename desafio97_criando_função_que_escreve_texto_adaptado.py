#criando uma função que recebe um texto como parâmetro e mostra um texto de tamanho adaptável. 


def escreva(texto):
    tamanho = len(texto) + 3
    print('~' * tamanho)
    print(f' {texto}' )
    print('~'* tamanho)

escreva('Edson Almeida')
escreva('Estudando python')
escreva('Programação é importante')