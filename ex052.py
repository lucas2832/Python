n = int(input('Digite um número para ser analizado: '))
multi = 0
div = 0
for i in range(1, n + 1):
    if n % i == 0:
        multi += 1
        div += 1
if multi == 2:
    print(f'O número {n} é primmo. ')
else:
    print(f'O número {n} possui {div} divisores, portanto não é um número primo.')
