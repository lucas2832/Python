nota1 = float(input('Qual sua nota em matemática? '))
nota2 = float(input('Qual sua nota em português? '))
media = (nota1 + nota2)/2
if media >= 6:
    print(f'Sua média é \033[32m{media:.2f}\033[m! ')
else:
    print(f'Sua média é \033[31m{media:.2f}\033[m!')
