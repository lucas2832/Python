peso = float(input('Para calcular seu IMC digite seu peso: '))
altura = float(input('Agora digite sua altura: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print(f'Seu IMC é {imc:.1f} e você está abaixo do seu peso ideal. ')
elif imc <= 25:
    print(f'Seu IMC é {imc:.1f} e você está no seu peso ideal. ')
elif imc <= 30:
    print(f'Seu IMC é {imc:.1f} e você está com sobrepeso. ')
elif imc <= 40:
    print(f'Seu IMC é {imc:.1f} e você está em estágio de obesidade. ')
elif imc > 40:
    print(f'Seu IMC é {imc:.1f} e você está em estágio de obesidade mórbida. ')
