km = float(input('Qual a distância da sua viagem? '))
if km >= 200:
    print(f'O valor da sua passagem será R${km * 0.45:.2f}.')
else:
    print(f'O valor da sua viagem será R${km * 0.5:.2f}')
