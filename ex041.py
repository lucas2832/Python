from datetime import date

ano = int(input(f'Qual o ano de nascimento? '))
idade = date.today().year - ano

if idade <= 9:
    print(f'O atleta tem {idade} anos e entrará na categoria mirim. ')
elif idade <= 14:
    print(f'O atleta tem {idade} anos e entrará na categoria infantil. ')
elif idade <= 19:
    print(f'O atleta tem {idade} anos e entrará na categoria junior. ')
elif idade <= 25:
    print(f'O atleta tem {idade} anos e entrará na categoria sênior. ')
elif idade > 25:
    print(f'O atleta tem {idade} anos e entrará na categoria master. ')
