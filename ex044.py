produto = float(input('Insira o valor do produto: '))

a = produto - (produto * 0.10)
b = produto - (produto * 0.05)
c = produto
d = produto + (produto * 0.20)

print('1) dinheiro/cheque (10% de desconto)\n'
      '2) à vista no cartão (5% de desconto)\n'
      '3) 2x cartão (preço anunciado)\n'
      '4) 3x ou mais no cartão (20% de juros)')

pagamento = int(input('Agora escolha dentre as opções a forma de pagamento: '))

if pagamento == 1:
    print(f'Escolhendo essa forma de pagamento você recebe um desconto de 10%,\n'
          f'e pagará, à vista, R${a:.2f}.')

elif pagamento == 2:
    print(f'Escolhendo essa forma de pagamento você receberá um desconto de 5%,\n'
          f'e pagará, à vista no cartão, R${b:.2f}.')

elif pagamento == 3:
    print(f'Escolhendo essa forma de pagamento você pagará o valor total anunciado do produto,\n'
          f'que é de R${c:.2f}, em duas parcelas de R${c / 2:.2f}.')

elif pagamento == 4:
    npar = int(input('Quantas parcelas? '))
    parcela = d / npar
    print(f'Escolhendo essa forma de pagamento o produto terá como juros um acréscimo de\n'
          f'20% ao seu valor total. Sendo assim, você pagará um total de R${d:.2f}, divido em {npar} parcelas iguais de R${parcela:.2f}.')
else:
    print('Opção de pagamento inválida. Tente novamente.')
