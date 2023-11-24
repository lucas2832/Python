palavras = ('programador', 'computador', 'monitor', 'mouse', 'teclado',
            'celular', 'relogio', 'processador', 'placa mae', 'placa de video')

for pos in range(len(palavras)):
    print(f'\nNa palavra "{palavras[pos]}" temos: ', end='')
    for letra in palavras[pos]:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')


    # Solução feita por mim:

    # if 'a' in palavras[pos]:
    #     print(end='a ')
    #
    # if 'e' in palavras[pos]:
    #     print(end='e ')
    #
    # if 'i' in palavras[pos]:
    #     print(end='i ')
    #
    # if 'o' in palavras[pos]:
    #     print(end='o ')
    #
    # if 'u' in palavras[pos]:
    #     print(end='u ')
