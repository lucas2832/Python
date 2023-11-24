exeloop = True
lista = []
cont = 0

while exeloop:
    numero = (input('Digite um número: '))
    if not numero.isnumeric():
        print('Informação inválida. ')
        continue

    numero = int(numero)
    cont += 1
    lista.append(numero)

    exeloop2 = True
    while exeloop2:
        continuarprograma = input('Deseja continuar? [S/N] ').strip().upper()

        if continuarprograma == 'S':
            print('=' * 30)
            exeloop2 = False
        elif continuarprograma == 'N':
            exeloop = False
            exeloop2 = False
        else:
            print('Escolha uma opção válida. ')

lista.sort(reverse=True)

print(f'Foram digitados {cont} números. ')
print(f'São eles: {lista}')

if 5 in lista:
    print(f'O número 5 se encontra na posição {lista.index(5)}')
else:
    print(f'A lista não possuie o número 5. ')

