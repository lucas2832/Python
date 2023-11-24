from time import sleep
nome = str(input('Qual seu nome? ')).strip().title()
print(f'É um prazer atende-lo, {nome}!')
sleep(1)
print('Preciso de algumas informações para saber se posso aprovar sua compra.')
sleep(1)
valor = float(input('Qual o valor da casa que pretende comprar? R$'))
sleep(1)
print('Certo!')
sleep(1)
tempo = int(input('Em quantos anos pretende pagar? '))
sleep(1)
print('Ok, só mais uma pergunta.')
sleep(1)
salario = float(input('Qual o seu salário atual? R$'))
print('Ok, estou analizando seus dados. ')
sleep(2)
prestacao = valor / (tempo * 12)
if prestacao > salario * 0.30:
    print(f'Nessas condições, o valor da sua prestação seria de R${prestacao:.2f}. Mas, infelizmente\n '
          f'esse valor excede 30% do seu salário, o que impossibilita a aprovação do seu empréstimo. ')
else:
    print(f'Parabéns!!! Seu empréstimo foi aprovado. A prestação será de R${prestacao:.2f}.')
