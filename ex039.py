from datetime import date

ano = int(input('Digite os quatro digitos do ano de seu nascimento: '))
idade = date.today().year - ano
alist = ano + 18

if idade < 18:
    print(f'Você está com {idade} anos.\nDaqui a {18 - idade} anos, em {alist}, '
          f'terá de se apresentar no serviço militar!')

elif idade == 18:
    print(f'Você está com {idade} anos. Já é hora de se apresenter às forçar armadas! ')

elif idade > 18:
    print(f'Você está com {idade} anos, já se passaram {idade - 18} anos da idade de seu alistamento.\n '
          f'Caso ainda não tenha se alistado, apresente-se o quanto antes! ')
