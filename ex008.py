m = float(input('Uma distância em metros: '))
cm = m * 100
mm = m * 1000
cm = round(cm, 10)
# print(f'Essa medida em centímetros é {cm:.10f} e em milímetros é {mm:.10f}!')
print(f'Essa medida em centímetros é \033[32m{cm}\033[m e em milímetros é \033[32m{mm}\033[m!')
