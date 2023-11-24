import math

l1 = float(input('Digite o valor do primeiro lado do triângulo: '))
l2 = float(input('Digite o valor do segundo lado do triângulo: '))
l3 = float(input('Digite o valor ddo terceiro lado do triângulo: '))
ce1 = l1 > math.fabs(l2 - l3)
ce2 = l1 < l2 + l3
if ce1 and ce2 == True:
    print('É possível formar um triângulo com esses valores! ')
else:
    print('Esses valores não formam um triângulo. ')
