n1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
c = 10
pa = n1

while c > 0:
    print(pa, end='')
    print('- 'if c > 1 else ' ', end='')
    pa += razao
    c -= 1
print('\nEsses são os 10 primeiros termos dessa PA. ')
