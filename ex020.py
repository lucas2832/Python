import random
n1 = input('Qual o primeiro aluno? ')
n2 = input('Qual o segundo aluno? ')
n3 = input('Qual o terceiro aluno ')
n4 = input('Qual o querto aluno? ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f'A ordem de apresentação do trabalho será {lista}')
