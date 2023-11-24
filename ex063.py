c = 0
n1 = 0
n2 = 1

while True:
    ntermos = (input('Quantos termos da sequência de Fibonacci deseja ver? '))

    if not ntermos.isnumeric():
        print('Digite apenas números inteiros.')
        continue

    intntermos = int(ntermos)
    print(f'Esses são os {intntermos} primeiros termos da sequência de Fibonacci: ')

    while c < intntermos:

        print(n1, end='')
        print(', ' if c < (intntermos - 1) else '', end='')
        sequencia = n1 + n2
        n1 = n2
        n2 = sequencia
        c += 1

    print(' - Fim!!!')
    break
