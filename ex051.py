n1 = int(input('Escolha o primeiro termo da PA: '))
razao = int(input('Escolha a razão da PA: '))
decimo = n1 + (10 - 1) * razao
for i in range(n1, decimo + razao, razao):
    print(f'{i}', end=' -')
print('Fim')
