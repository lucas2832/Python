import random

sorteio = random.randint(1, 3)
print('Vamos jogar Jokempô?\n'
      '1) Pedra\n'
      '2) Papel\n'
      '3) Tesoura ')
escolha = int(input('Boa sorte!!! Faça sua escolha digitando uma das opções acima: '))

if escolha == 1 and sorteio == 2:
    print('Eu escolhi papel, você perdeu!!')
elif escolha == 1 and sorteio == 3:
    print('Parabéns, você ganhou!!! Eu escolhi tesoura. ')
elif escolha == 1 and sorteio == 1:
    print('Nós empatamos!! Também escolhi pedra.')

elif escolha == 2 and sorteio == 2:
    print('Nós empatamos!! Também escolhi papel. ')
elif escolha == 2 and sorteio == 3:
    print('Você perdeu!! Eu escolhi tesoura. ')
elif escolha == 2 and sorteio == 1:
    print('Parabéns!! Você ganhou. Eu escolhi pedra.')

elif escolha == 3 and sorteio == 3:
    print('Nós empatamos!!! Também escolhi tesoura. ')
elif escolha == 3 and sorteio == 2:
    print('Que pena, você perdeu, Eu escolhi pedra. ')
elif escolha == 3 and sorteio == 1:
    print('Você perdeu. Eu escolhi pedra! ')

elif escolha != 1 or escolha != 2 or escolha != 3:
    print('Essa opção não é válida, tente novamente.')
