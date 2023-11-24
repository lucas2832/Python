exeloop = True
numeros = []

while exeloop:

    while True:
        escolha = input('Digite um número inteiro: ')

        if not escolha.isnumeric():
            print('Informação inválida. ')
            continue

        else:
            escolha = int(escolha)

            for i, v in enumerate(numeros):
                if v == escolha:
                    numeros.remove(escolha)
                    print('Valor já adicionado anteriormente. ')
            break

    numeros.append(escolha)

    while True:
        continuarprograma = input('Deseja adicionar mais um valor: [S/N] ').strip().upper()

        if continuarprograma == 'S':
            print('=' * 30)
            break

        if continuarprograma == 'N':
            print('=' * 30)
            exeloop = False
            break

        else:
            print('Opção inválida. Tente novamente')
            continue

    continue

numeros.sort()

print(f'Os valores digitados foram {numeros}. ')
