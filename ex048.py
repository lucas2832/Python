soma = 0
valores = 0
# for i in range(1, 500):
#     if i % 2 == 1 and i % 3 == 0:
#         soma += i
#         valores += 1
# Fazer de forma a exigir menos da máquina
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        valores += 1
print(f'A soma dos {valores} valores solicitados é {soma}. ')
