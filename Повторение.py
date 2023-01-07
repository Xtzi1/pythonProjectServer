per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
money = 100000

values = list(per_cent.values())
for i in values:
    i = i * money / 100
    deposit.append(int(i))
print('vse summi: ', deposit)

print(max(deposit))

def cycling(deposit):
    if len(deposit) == 1:
        return deposit[0]
    firstElement = deposit[0]
    tail = deposit[1:]
    tail_max = cycling(tail)
    if firstElement > tail_max:
        return firstElement
    else:
        return tail_max
print(cycling(deposit))