numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    escolha = (input('Digite em número entre 0 e 20: ')).strip()

    if not escolha.isnumeric():
        print('Informação inválida. ')
        continue

    escolha = int(escolha)

    if not 0 <= escolha <= 20:
        print('Tente novamente. ')
        continue
    break

print(f'Você digitou o número {numeros[escolha]}. ')
print('Fim!!!')
