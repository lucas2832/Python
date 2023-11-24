count = 0
soma = 0

while True:
    n = (input('Digite um número: [999 para encerrar] '))

    if not n.isnumeric():
        print('Por favor, digite um número. ')
        continue

    n = int(n)

    if n == 999:
        break

    soma += n
    count += 1

print(f'A soma dos {count} números digitados é {soma}.')
