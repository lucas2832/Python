# maiorpeso = 0
# menorpeso = 5000
#
# for i in range(0, 5):
#     peso = float(input('Peso da pessoa: '))
#     if peso > maiorpeso:
#         maiorpeso = peso
#     if peso < menorpeso:
#         menorpeso = peso
# print(f'o maior peso informado foi {maiorpeso}')
# print(f'O menor peso informado foi {menorpeso}')
# Minha solução

maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input(f'Digite o peso da {i}ª pessoa: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O menor peso informado foi {menor}kg e o maior foi {maior}kg.')
