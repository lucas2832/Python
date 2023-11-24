soma = 0
count1 = 0
count2 = 0
maisbarato = 0
nomemaisbarato = ''
exeloop = True

while exeloop:
    nome = input('Nome do produto: ').strip()

    while True:
        preco = (input('Valor do produto: R$')).strip()

        if not preco.isnumeric():
            print('Informação inválida. ')
            continue
        break

    preco = float(preco)
    count2 += 1
    soma += preco

    if preco >= 1000:
        count1 += 1

    if count2 == 1:
        maisbarato = preco
        nomemaisbarato = nome

    if maisbarato > preco:
        maisbarato = preco
        nomemaisbarato = nome

    while True:
        continuarprograma = input('Deseja continuar? [S/N] ').strip().upper()

        if continuarprograma == 'S':
            break

        elif continuarprograma == 'N':
            exeloop = False
            break

        else:
            print('Digite uma opção válida! [S/N] ')
            continue

print('-=' * 20)
print('Compra finalizada. ')
print('-=' * 20)

print(f'O total da compra foi {soma}. ')

if count1 == 1:
    print('1 produtp dessa lista custa mais de R$1000,00. ')
else:
    print(f'{count1} produtos dessa lista custam mais de R$1000,00. ')

print(f'O produto mais barato foi {nomemaisbarato}. ')

print('Fim!!!')
