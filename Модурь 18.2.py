# Задание 18.8.11
#
# Напишите программу, которая на вход принимает последовательность целых чисел,
# и возвращает True, если все числа ненулевые, и False, если хотя бы одно число равно 0.

# L = list(map(int, input().split()))
# print(all(L))
#
# функцию можно применить к спискам, словарям, кортежам с помощью конструкции map(что применить, к чему применить)
# def dictFunc(values):
#     return values*10
# values_dict = {1,2,3,4,5}
# finalitems = map(dictFunc, values_dict)
# print(list(finalitems))
# L = list(map(int, input().split()))
# print(all(L))
#
# M = list(map(int, input().split()))
# print(all(M))

# Напишите программу, которая на вход принимает последовательность целых чисел
# и возвращает True, если все числа равны нулю, и False, если найдется
# хотя бы одно ненулевое число. Разрешается использование только логических
# операторов и функций all([ ]) и any([ ]).
#
# a = list(map(int, input().split()))
# print(any(a) == 0)
#
# L = list(map(int, input().split()))
# print(not any(L))
#
# Генераторы списков — это специальный синтаксис, определяющий правила создания и заполнения списков.
# L = [ a for a in some_iter_obj if cond ]
#
# L = []
# for a in some_iter_obj:
#     if cond:
#         L.append(a)

# square = [i**2 for i in range(1, 11)]
# print(square)
#
# squareM = []
# squareN = []
# for i in square:
#     if i % 2 == 0:
#         squareM.append(i)
#     if i % 2 == 1:
#         squareN.append(i)
# print(squareM)
# print(squareN)

#Создать матрицу генераторами списков
# matrix = [[i+j for j in range(5)] for i in range(5)]
# print(matrix)
#
# При помощи генератора списков создайте таблицу умножения чисел от 1 до 10.
# tableUmnojeniya = [[i*j for j in range(1, 11)] for i in range(1, 11)]
# print(tableUmnojeniya)
# Приведенный выше пример пять раз запросит у пользователя данные для входа и запишет их в список.
# Здесь же можно использовать сразу преобразование в необходимый тип, если он заранее известен.
# L = [int(input()) for i in range(5)]
# print(L)

# Модифицируйте последний пример таким образом, чтобы в список сохранялось
# True, если элемент четный, и False, если элемент нечетный.
# L = [int(input()) % 2 == 0 for i in range(5)]
# print(L)
#
# Тру если хотя бы одно четное
# L = [int(input()) % 2 == 0 for i in range(5)]
# print(any(L))

# Подумайте, как нужно записать логическое выражение, используя all([ ]) и any([ ])
# над списком четности, если его результат будет истинным тогда и только тогда,
# когда в списке есть хотя бы один четный и хотя бы один нечетный элемент.
# L = [int(input()) % 2 == 0 for i in range(5)]
# print((any(L)) and (not all(L)))
#
# Умножить список на число
# n = [i for i in range(6)]
# b = 2
# m = []
# for i in n:
#     m.append(i*b)
# print(n)
# print(m)
#
# L = [i for i in range(10)]
# # 0 1 2 3 4 5 6 7 8 9
# M = [i for i in range(10,0,-1)]
# # 10 9 8 7 6 5 4 3 2 1
# N = [a*b for a,b in zip(L,M)]
# print(N)
#
# Реализуйте программу, которая сжимает последовательность символов. На вход подается последовательность вида:
# aaabbccccdaa
# Необходимо вывести строку, состоящую из символов и количества повторений этого символа. Вывод должен выглядеть как:
# a3b2c4d1a2

# text = input()  # получаем строку
#
# first = text[0]  # сохраняем первый символ
# count = 0  # заводим счетчик
# result = ''  # и результирующую строку
# for c in text:
#     if c == first:  # если символ совпадает с сохраненным,
#         count += 1  # то увеличиваем счетчик
#     else:
#         result += first + str(count)  # иначе - записываем в результат
#         first = c  # и обновляем сохраненный символ с его счетчиком
#         count = 1
# result += first + str(count)  # и добавляем в результат последний символ
# print(result)


# a = input('aaabbccccdaa')
# first_elem = a[0]
# count = 0
# result = ''
#
# for i in a:
#     if i == first_elem:
#         count += 1
#     else:
#         result += first_elem + str(count)
#         first_elem = i
#         count = 1
# result += first_elem + str(count)
# print(result)

# Конструкция list(range(start, end, step)) позволяет получить
# последовательность (список) целых чисел,
# начинающуюся со start и заканчивающуюся в end-1 с шагом step.

# S = 0  # заводим переменную-счетчик, в которой мы будем считать сумму
# N = 5
# for i in range(1, N+1):
#     S = S + i
# print(S)
#
# P = 1 # заводим переменную-счетчик, в которой мы будем считать произведение, подумайте чему она должна быть равна
# V = 5
# for b in range(1, V+1):
#     P *= b
# print(P)

# напечатать лесенку
# n = 10
# for i in range(0, n+1):
#     print('*'*i)
#
# Напишите цикл, который будет складывать натуральные числа, пока их сумма не превысит 500.

# S = 0
# n = 1
# while S < 500:
#     S += n
#     n += 1
#     print('еще считаю..')
# print(S)

# n = 1
# while n**2 < 1000:
#     n += 1
# print(n)

# Напишите цикл с использованием бесконечного цикла whilе с постусловием,
# который возводит натуральные числа в квадрат, пока результат меньше 1000.
# n = 1
# while True:
#     if n**2 > 1000:
#         print("последнее число", n-1)
#         break
#     n +=1
# print(n)
#
# L = [i*5 for i in range(1,-50,-10)]
# print(L)

# G = 2
# V = 3
# matrix = [
#     [0, 1, 2],
#     [3, 4, 5],
# ]
# for i in range(G):
#     for j in range(V):
#         print(matrix[i][j], end=" ")
#     print(" ")

# Дана двумерная матрица 3x3. Определите максимум и минимум каждой строки, а также их индексы.
# random_matrix = [
#    [9, 2, 1],
#    [2, 5, 3],
#    [4, 8, 5]
# ]
# min_value_rows = []  # здесь будут храниться минимальные значения для каждой строки
# min_index_rows = []  # здесь будут храниться индексы минимальных значений для каждой строки
# max_value_rows = []  # здесь будут храниться максимальные значения для каждой строки
# max_index_rows = []  # здесь будут храниться индексы максимальных значений для каждой строки
# for i in random_matrix:
#     max_index = 0
#     min_index = 0
#     max_value = i[max_index]
#     min_value = i[min_index]
#     for j in range(len(i)):
#         if i[j] > max_value:
#             max_value = i[j]
#             max_index = j
#         if i[j] < min_value:
#             min_value = i[j]
#             min_index = j
#     min_value_rows.append(min_value)
#     min_index_rows.append(min_index)
#     max_value_rows.append(max_value)
#     max_index_rows.append(max_index)
# print(max_value_rows)
# print(max_index_rows)
# print(min_value_rows)
# print(min_index_rows)

# list_ = [-5, 2, 4, 8, 12, -7, 5]
# for i in range(len(list_)):  # равносильно выражению for i in [0, 1, 2, 3, 4, 5, 6]:
#     print("Индекс элемента: ", i)
#     print("Значение элемента: ", list_[i])  # с помощью индекса получаем значение элемента
#     print("---")
# print("Конец цикла")

# spiska = [i for i in range(10)]
# for i, value in enumerate(spiska):
#     print(enumerate(spiska))

# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Функция enumerate возвращает данные в виде кортежей,
# # где на первом месте стоит индекс, а затем значение
# # [(0, -5), (1, 2), (2, 4), ...]
# for i, value in enumerate(list_):
#     print("Индекс элемента: ", i)
#     print("Значение элемента: ", value)  # с помощью индекса получаем значение элемента
#     print("---")
# print("Конец цикла")

# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Объявим переменную, в которой будем хранить индекс отрицательного элемента
# index_negative = None
#
# for i, value in enumerate(list_):
#     if value < 0:
#         print("Отрицательное число: ", value)
#         index_negative = i  # перезаписываем значение индекса
#         print("Новый индекс отрицательного числа: ", index_negative)
#     else:
#         print("Положительное число: ", value)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: индекс последнего отрицательного элемента = ", index_negative)
# подсчет кол-во повторений символов в тексте (без пробелов, не чувствительно к регистру)
# text = """
# У лукоморья дуб зелёный;
# Златая цепь на дубе том:
# И днём и ночью кот учёный
# Всё ходит по цепи кругом;
# Идёт направо -- песнь заводит,
# Налево -- сказку говорит.
# Там чудеса: там леший бродит,
# Русалка на ветвях сидит;
# Там на неведомых дорожках
# Следы невиданных зверей;
# Избушка там на курьих ножках
# Стоит без окон, без дверей;
# Там лес и дол видений полны;
# Там о заре прихлынут волны
# На брег песчаный и пустой,
# И тридцать витязей прекрасных
# Чредой из вод выходят ясных,
# И с ними дядька их морской;
# Там королевич мимоходом
# Пленяет грозного царя;
# Там в облаках перед народом
# Через леса, через моря
# Колдун несёт богатыря;
# В темнице там царевна тужит,
# А бурый волк ей верно служит;
# Там ступа с Бабою Ягой
# Идёт, бредёт сама собой,
# Там царь Кащей над златом чахнет;
# Там русский дух... там Русью пахнет!
# И там я был, и мёд я пил;
# У моря видел дуб зелёный;
# Под ним сидел, и кот учёный
# Свои мне сказки говорил.
# """
#
# text = text.lower()
# text = text.replace(' ', '')
# text = text.replace('\n', '')
# count = {}
# for symbol in text:
#     if symbol in count:
#         count[symbol] += 1
#     else:
#         count[symbol] = 1
# for key, value in count.items():
#     print(f'{key} встречается {value} раз(а)')

# Проверьте, является ли заданное число степенью тройки.
#
# Чтобы число было степенью тройки, необходимо, чтобы при его делении на
# 3 мы в остатке всегда получали
# 0. И как только мы дойдем до 1, значит число является степенью тройки.
# Если на каком-то шаге остаток не равен 0, то число не является степенью
# тройки, и дальше проверять нет необходимости.
#
# n = 3
# while True:
#     if n % 3 == 0:
#         n = n // 3
#         if n == 1:
#             print('Является')
#             break
#     else:
#         print('Не является')
#         break
#
# Допишите функцию check_h так, чтобы она проверяла гипотезу Сиракуз для числа n.
# Гипотеза Сиракуз заключается в том, что любое натуральное число можно свести к 1,
# если повторять над ним следующие действия:
# если число четное, то разделить его пополам,
# если нечетное - умножить на 3, прибавить 1 и результат разделить на 2.
# n = 11
# def check_h(n):
#     while n > 1:
#         if n % 2 == 0:
#             n = n // 2
#         elif n % 2 == 1:
#             n = ((n * 3) + 1) / 2
#         if n == 1:
#             break
#         return True
#     return False
# print(check_h(n))


# В клетке находятся фазаны и кролики. Известно, что у них 35 голов и 94 ноги. Узнайте число фазанов и число кроликов.
# heads = 35
# legs = 94
# for rabbits in range(heads+1):
#     for pheasant in range(heads+1):
#         if (rabbits + pheasant) > heads or \
#                 (rabbits*4 + pheasant*2) > legs:
#                 continue
#         if (rabbits + pheasant) == heads and \
#                 (rabbits*4 + pheasant*2) == legs:
#                 print('Rabbits: ', rabbits)
#                 print('Pheasants: ', pheasant)
#                 print('---')
#
# Допишите функцию print_ladder так, чтобы она для числа n печатала лесенку следующего типа:
#
# n = 3 * ** ***
# n = 4 * ** *** ****
