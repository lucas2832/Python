contador = 1
fatorial = 1
nisnumeric = True
exeloop = True
exeloop2 = True
continuarprograma = ''

while exeloop:
    n = input('Digite um número inteiro: ').strip()
    nisnumeric = n.isnumeric()
    if not nisnumeric:
        print('Digite um valor númerico.')
        print('=' * 30)
        continue

    n = int(n)

    while contador <= n:
        fatorial *= contador
        contador += 1
    print(f'O valor de {n}! é {fatorial}.')

    while exeloop2:
        continuarprograma = input('Deseja continuar? [S/N]').strip().upper()
        if continuarprograma == 'S':
            print('=' * 30)
            break

        if continuarprograma == 'N':
            exeloop = False
            break

        else:
            print('Digite uma opção válida. [S/N] ')
            print('=' * 30)
            continue

    contador = 1
    fatorial = 1

    continue

print('Fim!')
