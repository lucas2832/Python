from bisect import insort
listanum = []

# for i in range(0, 5):
#     n = int(input('Digite um número: '))
#     insort(listanum, n)

for i in range(0, 5):
    n = int(input('Digite um número: '))
    if i == 0 or n > listanum[-1]:
        listanum.append(n)
    else:
        pos = 0
        while pos <= len(listanum):
            if n <= listanum[pos]:
                listanum.insert(pos, n)
                break
            pos += 1
print(listanum)
