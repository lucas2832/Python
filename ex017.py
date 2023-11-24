from math import *
co = float(input('Qual o valor do cateto oposto? '))
ca = float(input('Qual o valor do cateto adjacente? '))
# h = sqrt(co ** 2 + ca ** 2)
h = hypot(co, ca)
print(f'No triângulo de cateto oposto igual a {co} e cateto adjacente igual a {ca} a hipotenusa vale {h}.')
