n1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
c = 10
pa = n1
exeloop = True
exeloop2 = True

while exeloop:
    while c > 0:
        print(pa, end='')
        print(', 'if c > 1 else ' ', end='')
        pa += razao
        c -= 1
    print('\nEsses são os 10 primeiros termos dessa PA. ')

    while exeloop2:
        continuar = str(input('\nO que deseja fazer?\n'
                              '[1] Mostrar mais termos dessa PA.\n'
                              '[2] Encerrar programa.\n'
                              'Escolha uma opção: '))

        if continuar == '1':
            termosadd = int(input('Quantos termos a mais deseja mostrar? '))
            c = termosadd
            n1 = n1 + (10 - 1) * razao

            while c > 0:
                print(pa, end='')
                print('- ' if c > 1 else ' ', end='')
                pa += razao
                c -= 1

        elif continuar == '2':
            exeloop = False
            exeloop2 = False

        else:
            print('Digite uma opção válida. ')
            continue

print('Fim!!!')
