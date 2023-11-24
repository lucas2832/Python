listagem = ('Lápis', 1.50,
            'Caneta', 2.00,
            'Caderno', 14.90,
            'Régua', 3.49,
            'Corretivo', 5.90,
            'Borracha', 2.00,
            'Compasso', 8.90,
            'Mochila', 149.90)

print('=' * 40)
print('Lista de preços'.center(30))
print('=' * 40)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30} R${listagem[pos + 1]:>6.2f}')

print('=' * 40)