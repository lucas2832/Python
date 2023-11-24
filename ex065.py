count = 0
soma = 0
maior = 0
menor = 0
exeloop = True
continuarprograma = True

while exeloop:
    n = float(input('Digite um número: '))
    count += 1
    soma += n

    if count == 1:
        maior = n
        menor = n

    if maior < n:
        maior = n

    if menor > n:
        menor = n

    while continuarprograma:
        addnumero = input('Deseja adicionar mais um número? [S/N] ').strip().upper()

        if addnumero == 'S':
            break

        if addnumero == 'N':
            exeloop = False
            break

        else:
            print('Digite uma opção válida. [S/N] ')
            continue

    continue

media = soma / count

print(f'A média dos valores digitados é {media}. O maior valor digitado é {maior} e o menor é {menor} ')
