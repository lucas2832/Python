from math import fabs
l1 = float(input('Digite o primeiro lado do triângulo: '))
l2 = float(input('Digite o segundo lado do triângulo: '))
l3 = float(input('Digite o terceiro lado do triângulo: '))
co1 = l1 > fabs(l2 - l3)
co2 = l1 < l2 + l3
if l1 == l2 == l3:
    print('Esses valores formam um trângulo equilátero. ')
elif co1 and co2 == True:
    if l1 == l2 or l1 == l3 or l2 == l3:
        print('Esses valores formam um triângulo isóscles. ')
    elif l1 != l2 != l3 != l1:
        print('Esses valores formam um trângulo escaleno. ')
else:
    print('Esses valores não formam um triângulo. ')
