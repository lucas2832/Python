expressao = input('Digite uma expressão: ')
pilha = []

for i in expressao:
    if i == '(':
        pilha.append('(')
    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')

if len(pilha) == 0:
    print('A expressão é válida! ')
else:
    print('A espressão está errada! ')

