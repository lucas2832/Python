nota50 = 0
nota20 = 0
nota10 = 0
nota1 = 0

print('-=' * 30)
print('Nesse caixa eletrônico estão disponíveis cédulas de R$50, R$20, R$10 e R$1. ')

while True:
    valorsacado = (input('Quanto deseja sacar? '))

    if not valorsacado.isnumeric():
        print('Informação inválida. ')
        continue
    else:
        valorsacado = int(valorsacado)
        break

if valorsacado > 50:
    nota50 = valorsacado // 50
valorsacado = valorsacado - (nota50 * 50)

if valorsacado > 20:
    nota20 = valorsacado // 20
valorsacado = valorsacado - (nota20 * 20)

if valorsacado > 10:
    nota10 = valorsacado // 10
valorsacado = valorsacado - (nota10 * 10)

if valorsacado >= 1:
    nota1 = valorsacado

print('-=' * 30)
print('Você receberá: ')

if nota50 >= 1:
    print(f'{nota50} cédula(s) de R$50 ')

if nota20 >= 1:
    print(f'{nota20} cédula(s) de R$20 ')

if nota10 >= 1:
    print(f'{nota10} cédula(s) de R$10 ')

if nota1 >= 1:
    print(f'{nota1} cédula(s) de R$1 ')

print('-=' * 30)
print('Obrigado por usar nossos caixas eletrônicos. Volte sempre! ')
