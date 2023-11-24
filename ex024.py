name = str(input('Digite o nome da sua cidade: ')).strip()
divisao = name.split()
print('Começa com a palavra Santo', end='? ')
if divisao[0].lower() == 'santo':
    print('Sim')
else:
    print('Não')
