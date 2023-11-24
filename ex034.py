salario = float(input('Qual o seu salário atual? '))
a1 = salario + (salario * 0.10)
a2 = salario + (salario * 0.15)
if salario > 1250:
    print(f'Seu salário atual é R${salario}, e com o aumento de 10% será R${a1}. ')
if salario <= 1250:
    print(f'Seu salário atual é R${salario}, e com o aumento de 15% será R${a2}.')
