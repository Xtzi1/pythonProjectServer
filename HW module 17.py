# Задание 17.7.3

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
money = int(input('Введите сумму: '))
values_of_per_cent = list(per_cent.values())

for i in values_of_per_cent:
    i = i * money / 100
    deposit.append(int(i))

print('Все суммы: ', deposit)

#Решение с помощью метода max()
print('Максимальная сумма, которую вы можете заработать — ', max(deposit))

#Решение с помощью рекурсии
def custom_max(deposit):
    if len(deposit) == 1:
        return deposit[0]
    first_elem = deposit[0]
    tail = deposit[1:]
    tail_max = custom_max(tail)
    if first_elem > tail_max:
        return first_elem
    else:
        return tail_max

print('Максимальная сумма, которую вы можете заработать — ', custom_max(deposit))
