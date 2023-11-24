exeloop = True
dados = []
pessoas = []
peso = ''
maispesado = maisleve = 0
cont = 0
nomemaispesado = []
nomemaisleve = []

while exeloop:
    looppeso = True
    continuarprograma = True
    cont += 1
    nome = (input('Nome: ').strip().title())
    dados.append(nome)

    while looppeso:
        peso = input('Peso: ').strip()
        if not peso.isnumeric():
            print('Informação inválida! ')
            continue
        looppeso = False

    peso = int(peso)
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()
    if cont == 1:
        maisleve = peso
        maispesado = peso
        nomemaisleve.append(nome)
        nomemaispesado.append(nome)

    if peso > maispesado:
        maispesado = peso
        nomemaispesado.clear()
        nomemaispesado.append(nome)
    elif peso == maispesado:
        nomemaispesado.append(nome)

    if peso < maisleve:
        maisleve = peso
        nomemaisleve.clear()
        nomemaisleve.append(nome)
    elif peso == maisleve:
        nomemaisleve.append(nome)

    while continuarprograma:
        opcao = input('Deseja adicionar mais uma pessoa? [S/N] ').strip().lower()
        if opcao == 's':
            continuarprograma = False
        elif opcao == 'n':
            exeloop = False
            continuarprograma = False
        else:
            print('Escolha uma opção válida: S(sim) ou N(não) ')
            print('=' * 30)
            continue

    print('=' * 30)

print(f'{cont} pessoas foram cadastradas. ')
print(f'A mais pesada tem {maispesado}kg. Peso de {nomemaispesado}. ')
print(f'A mais leve tem {maisleve}kg. Peso de {nomemaisleve}. ')
