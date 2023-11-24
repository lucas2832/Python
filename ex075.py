while True:
    n1 = (input('Digite um número: ')).strip()

    if not n1.isnumeric():
        print('Digite um número inteiro.')
        continue
    break
n1 = int(n1)

while True:
    n2 = (input('Digite outro número: '))

    if not n2.isnumeric():
        print('Digite um número inteiro.')
        continue
    break
n2 = int(n2)

while True:
    n3 = (input('Digite o terceiro número: '))

    if not n3.isnumeric():
        print('Digite um número inteiro.')
        continue
    break
n3 = int(n3)

while True:
    n4 = (input('Digite o último número: '))

    if not n4.isnumeric():
        print('Digite um número inteiro.')
        continue
    break
n4 = int(n4)


tupla = (n1, n2, n3, n4)

print(f'Você digitou os valores {tupla}. ')

if tupla.count(9) == 0:
    print('Nenhum número 9 foi digitado. ')
elif tupla.count(9) == 1:
    print('O número 9 foi digitado uma vez. ')
else:
    print(f'O número 9 foi digitado {tupla.count(9)} vezes')

if tupla.count(3) >= 1:
    print(f'Na posição {tupla.index(3) + 1} foi digitado o primeiro número 3. ')
else:
    print('Nenhum número 3 foi digitado. ')

print('Os valores pares digitados foram: ', end='')

if n1 % 2 == 0:
    print(n1, end=' ')

if n2 % 2 == 0:
    print(n2, end=' ')

if n3 % 2 == 0:
    print(n3, end=' ')

if n4 % 2 == 0:
    print(n4, end=' ')
