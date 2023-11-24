n = int(input('Digite um número para saber sua tabuada: (Ou digite um número negativo para encerrar) '))

while n > 0:
    for i in range(11):
        print(f'{n} x {i} = {n * i}')

    n = int(input('Digite um número para saber sua tabuada: (Ou digite um número negativo para encerrar) '))

print('Fim!!!')
