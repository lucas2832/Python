n = float(input('Quanto dinheiro você possue? R$'))
dolar = n / 5.22
euro = n / 5.50
libra = n / 6.37
print(f'Com essa quantia você consegue comprar \033[32m{dolar:.2f}\033[m dolares, \033[32m{euro:.2f}\033[m euros e '
      f'\033[32m{libra:.2f}\033[m libras esterlinas. ')
