import random
a = input('Digite o nome do aluno: ')
b = input('Digite o nome do aluno: ')
c = input('Digite o nome do aluno: ')
d = input('digite o nome do aluno: ')
lista = [a, b, c, d]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}!! ')
