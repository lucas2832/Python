numeros = []
maior = 0
menor = 0

for c in range(0, 5):
    numeros.append(int(input(f'Digite o valor da posição {c}: ')))

    if c == 0:
        maior = menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]

        if numeros[c] < menor:
            menor = numeros[c]

    c += 1
print('=' * 30)

print(f'Você digitou os números {numeros}.')

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i}... ', end=' ')

print(f'\nO menor valor foi {menor} nas posições ', end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i}... ', end='')
print()
print('=' * 30)