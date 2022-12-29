#criando uma função que recebe dois números no parâmetro e que os calcula em fatorial.


def fatorial(a, b=False):
    """
    ->Calcua o fatorial de um número.
    :param a: O número a ser calculado.
    :param b: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(a, 0, -1):
        if b:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

fatorial(10, 8)