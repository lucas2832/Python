# masculino = 1
# feminino = 2
hmaisvelho = ''
maioridadehomem = 0
mulher = 0
itotal = 0

for i in range(0, 4):
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = int(input('Sexo:\n(1) Masculino\n(2) Feminino\nEscolha uma opção: '))
    print('=' * 30)

    if sexo == 1 and idade > maioridadehomem:
        hmaisvelho = nome

    if sexo == 2 and idade < 20:
        mulher += 1

    itotal += idade

print(f'A média de idade do grupo é {itotal / 4:.2f}.')
print(f'O homem mais velho é {hmaisvelho}.')
print(f'{mulher} mulher(es) tem menos de 20 anos. ')
