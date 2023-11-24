lista = [[], []]

for i in range(0, 7):
    numero = int(input(f'Digite o {i + 1}° valor: '))

    if numero % 2 == 0:
        lista[0].append(numero)
    if numero % 2 == 1:
        lista[1].append(numero)

lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram {lista[0]}. ')
print(f'Os valores ímpares digitados foram {lista[1]}. ')