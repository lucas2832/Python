nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print(f'Sua média é \033[31m{media}\033[m. Você será reprovado. ')
elif media == 5 or media <= 6.9:
    print(f'Sua média foi {media}. Você precisará fazer a recuperação. ')
elif media >= 7:
    print(f'Sua média é {media}. Parabéns!!! Você foi aprovado!')
