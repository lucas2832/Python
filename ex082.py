lista = []
listaimpar = []
listapar = []
exeloop1 = True

while exeloop1:
    numeros = (input('Digite um número inteiro: '))
    if not numeros.isnumeric():
        print('Informaçao inválida. ')
        continue
    numeros = int(numeros)

    lista.append(numeros)
    if numeros % 2 == 0:
        listapar.append(numeros)
    elif numeros % 2 == 1:
        listaimpar.append(numeros)

    exeloop2 = True
    while exeloop2:
        continuarprograma = input('Deseja continuar? [S/N] ').strip().upper()
        if continuarprograma == 'S':
            print('=' * 30)
            exeloop2 = False
        elif continuarprograma == 'N':
            print('=' * 30)
            exeloop1 = False
            exeloop2 = False
        else:
            print('Informação inválida. ')

print(f'Foram digitados os números {lista}. ')
print(f'Dentre eles, {listapar} são pares e {listaimpar} são ímpares. ')
