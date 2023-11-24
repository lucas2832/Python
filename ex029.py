v = int(input('Qual a velocidade do veículo? '))
km = v - 80
multa = 7 * km
if v > 80:
    print(f'Você está {km} km/h acima do limite de velocidade, por isso receberá uma multa de R${multa}.')
else:
    print('Tudo certo, prossiga com sua viagem.')
