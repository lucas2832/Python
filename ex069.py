count1 = 0
count2 = 0
count3 = 0
exeloop = True

while exeloop:
    while True:
        idade = (input('informe sua idade? '))

        if not idade.isnumeric():
            print('Informação inválida. ')
            continue

        else:
            break

    idade = int(idade)

    while True:
        sexo = input('Informe o sexo: [F/M] ').strip().upper()
        if sexo == 'F':
            break

        elif sexo == 'M':
            break

        else:
            print('Informação invalida. ')
            continue

    if idade >= 18:
        count1 += 1

    if sexo == 'M':
        count2 += 1

    elif sexo == 'F' and idade < 20:
        count3 += 1

    while True:
        continuarprograma = input('Deseja cadastrar mais um usuário? [S/N] ').strip().upper()

        if continuarprograma == 'S':
            break

        elif continuarprograma == 'N':
            exeloop = False
            break

        else:
            print('Digite uma opção válida! [S/N] ')
            continue

    print('-=' * 30)

print('Dos usuários cadastrados temos: ')

if count1 >= 1:
    print(f'{count1} com 18 anos ou mais. ')

if count2 == 1:
    print('1 homem.')
elif count2 > 1:
    print(f'{count2} homens. ')

if count3 == 1:
    print('1 mulher com menos de 20 anos. ')
elif count3 > 1:
    print(f'{count3} mulheres com menos de 20 anos. ')