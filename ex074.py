from random import randint

numeros = ''
print('Os valores sorteados foram: ', end='')
t = tuple()

for i in range(0, 5):
    n = randint(0, 10)
    t = t + (n,)

ordem = sorted(t)
print(t)
print(f'O maior número sorteado foi {ordem[4]}. ')
print(f'O menor número sorteado foi {ordem[0]}. ')
