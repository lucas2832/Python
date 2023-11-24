continuarprograma = True
exeprograma = True
sexo = ''

while exeprograma:
    sexo = str(input('Informe o sexo: [S/M] ')).strip().upper()[0]

    if sexo != 'F' and sexo != 'M':
        print('Digite um opção válida. ')
        print('=' * 30)
        continue

    if sexo == 'F':
        print('O sexo escolhido foi feminino. ')

    if sexo == 'M':
        print('O sexo escolhido foi masculino. ')

    while continuarprograma:
        finalizar = input('Deseja continuar? [S/N] ').strip().upper()[0]

        if finalizar == 'S':
            print('=' * 30)
            break

        if finalizar == 'N':
            exeprograma = False
            break

        else:
            print('Digite uma opção válida. ')
            print('=' * 30)
            continue

    continue

print('Fim!!')
