from random import randint

tentativas = 0

n = int(input('Tente adivinhar o número escolhido, entre 0 e 10: '))
aleatorio = randint(0, 10)

while n != aleatorio:

    if n < aleatorio:
        print('Mais... tente novamente. ')
    elif n > aleatorio:
        print('Menos... Tente novamente. ')

    n = int(input('Você errou, tente novamente: '))
    tentativas += 1

if tentativas == 0:
    print('Parabéns!!! Você acertou.')
else:
    print(f'Você acertou, mas foram necessárias {tentativas} tentativas. ')
