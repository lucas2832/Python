preco = float(input('Qual o preço do produto? '))
promo = preco - (preco * 0.05)
promo = round(promo, 2)
print(f'Na liquidação o preço desse produto é {promo} reais. ')
