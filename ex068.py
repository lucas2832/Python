from random import randint

count = 0
resultado = 0
exeloop = True

print('Vamos jogar par ou impar? ')

while exeloop:
    numeroescolhido = (input('Ecolha um número: '))
    computador = randint(0, 10)

    if not numeroescolhido.isnumeric():
        print('Por favor, digite um número inteiro. ')
        continue

    numeroescolhido = int(numeroescolhido)
    soma = numeroescolhido + computador
    count += 1

    while True:
        escolha = input('Você deseja escolher par ou impar? [P/I] ').strip().upper()
        if escolha == 'P' and soma % 2 == 0:
            print(f'Parabéns!!! Você venceu. Eu escolhi {computador} e a soma deu {soma}. Vamos novamente!')
            break

        elif escolha == 'I' and soma % 2 == 0:
            print(f'Que pena, você perdeu! Eu escolhi {computador} e a soma deu {soma}.')
            exeloop = False
            break

        elif escolha == 'P' and soma % 2 == 1:
            print(f'Que pena, você perdeu! Eu escolhi {computador} e a soma deu {soma}.')
            exeloop = False
            break

        elif escolha == 'I' and soma % 2 == 1:
            print(f'Parabéns!!! Você venceu. Eu escolhi {computador} e a soma deu { soma}. Vamos novamente!')
            break

        else:
            print('Digite uma opção válida. [P/I] ')
            continue

if count > 1:
    print(f'Você obteve {count} vitórias consecutivas! ')

print('Fim!!!')
