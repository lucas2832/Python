nome = str(input('Digite seu nome: ')).strip()
divisao = nome.split()
junto = ''.join(divisao)
print(f'Apenas letras maiúsculas: {nome.upper()}')
print(f'Apenas letras minúsculas: {nome.lower()}')
print(f'Quantidade de letras do primeiro nome: {len(divisao[0])}')
print(f'Quantidade de letras do nome completo: {len(junto)}')