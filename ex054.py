from datetime import date
maior = 0
menor = 0
for i in range(0, 7):
    ano = int(input('Digite ano de nascimento: '))
    idade = date.today().year - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoa(s) dessa lista já atingiram a maioridade. ')
print(f'{menor} pessoa(s) ainda não atingiram a maioridade. ')
