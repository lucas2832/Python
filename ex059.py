opcao = 0
continuarprograma = 0
opcaoenumerica = True
opcaomenuvalida = True
executarloop = True

while continuarprograma != 5:

    n1 = input('Digite o primeiro valor: ').strip()
    while not n1.isnumeric():
        n1 = input('Digite apenas valores númericos: ').strip()
    n1 = float(n1)

    n2 = input('Digite o segundo valor: ')
    while not n2.isnumeric():
        n2 = input('Digite apenas valores númericos: ').strip()
    n2 = float(n2)
    print('=' * 25)

    while executarloop:
        opcao = input('O que deseja fazer?\n'
                          '[1] Somar.\n'
                          '[2] Multiplicar.\n'
                          '[3] Maior.\n'
                          '[4] Escolher novos valores.\n'
                          '[5] Sair do programa.\n'
                          'Escolha uma opção: ').strip()

        opcaoenumerica = opcao.isnumeric()
        if not opcaoenumerica:
            print('Digite um valor numérico. ')
            print('=' * 25)
            continue
            
        opcao = int(opcao)

        opcaomenuvalida = 1 <= opcao <= 5
        if not opcaomenuvalida:
            print('Digite um número entre 1 e 5')
            print('=' * 25)
            continue
        executarloop = False

    if opcao == 1:
        print(f'{n1} + {n2} = {n1 + n2}')

    if opcao == 2:
        print(f'{n1} x {n2} = {n1 * n2}')

    if opcao == 3:
        if n1 > n2:
            print(f'O maior valor digitado foi {n1}')
        else:
            print(f'O maior valor digitado foi {n2}')

    if opcao == 4:
        print('=' * 25)
        continue

    if opcao == 5:
        continuarprograma = 5

print('Fim!!')
