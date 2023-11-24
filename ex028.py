import random
# from time import sleep
n = int(input('Tente adivinhar o número escolhido: '))
aleatorio = random.randint(0, 5)
# print('Processando...')
# sleep(3)
if aleatorio == n:
    print('Parabéns, você acertou!')
else:
    print(f'Que pena, você errou! O número escolhido foi {aleatorio}.')
