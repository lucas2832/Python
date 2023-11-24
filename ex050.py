s = 0
for i in range(0, 6):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        s = s + n
if s == 0:
    print('Nenhum valor par foi digitado. ')
else:
    print(f'A soma dos valores pares digitados é {s}.')