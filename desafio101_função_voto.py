#criando uma função que indica se, com base na idade digitada, o usuário deve votar ou não.



def voto(ano):
    from datetime import date
    hoje = date.today().year
    idade = hoje - ano
    if idade >= 16 and ano < 18:
        print(f'Você tem {idade} anos de idade e sua votação é opcional')
    elif idade < 18:
        print(f'Você tem {idade} anos de idade e não é obrigado a votar')
    else:
        print(f'Você tem {idade} anos de idade e tem idade para votar')

voto(2019)