import emoji
from time import sleep

print('Contagem regressiva para os fogos')
for i in range(10, -1, -1):
    sleep(1)
    print(i)
sleep(1)
print(emoji.emojize(':fireworks:' * 10))

