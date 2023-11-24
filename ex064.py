count = 0
soma = 0
exeloop = True

while exeloop:
    n = int(input('Digite um número inteiro: [ 999 para encerrar] '))
    if n != 999:
        count += 1
        soma += n

    if n == 999:
        exeloop = False

print(f'a soma dos {count} números digitados é {soma}.')
