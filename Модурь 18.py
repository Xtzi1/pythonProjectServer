# a = 1
# c = 1
# b = [2, c, 6]
#
# if a in b:
#     print('Lol')
# else:
#     print('combaya')
#
# if a is c:
#     print('YEAH')
# else:
#     print('NON')
#
# print(not True)
# x = 2000
# def is_leap_year(x):
#     return (x % 4 == 0) or (x % 400 == 0) and (x % 100 != 0)
# print(is_leap_year(x))
#
# print('3' and '7' in str(123456789))
#
# a = 7
# b = 9 + a
# print('a = F(", b,")')

# isRainy = False
# heavyRain = True
#
# if isRainy:
#     if heavyRain:
#         print('berem zont')
#     else:
#         print('dozhdevik')
# else:
#     print('tak poidy')
#
# try:  # Добавляем конструкцию try-except для отлова нашей ошибки
#     print("Перед вводом")
#     a = int(input("введите число: "))
# except ValueError as e:  # Добавляем тип именно той ошибки которую хотим отловить.
#     print('Вы ввели не число')  # Выводим информацию об ошибке
# else:
#     print('Вы ввели: ', (a))
# finally:
#     print("Выход из программы")
#
# Запишите вместо вопросительных знаков выражение, которое вернет True, когда каждое из чисел А и В нечетное.
#
# A = 2
# B = 4
#
# def are_both_odd(A, B):
#     if not A % 2 == 0 and not B % 2 == 0:
#         return True
#     else:
#         return False
# print(are_both_odd(A, B))
#
# def are_both_odd2(A, B):
#     return (A % 2 != 0) and (B % 2 != 0)
#
# print(are_both_odd2(A, B))

# if A % 2 == 1 and B % 2 == 1:
#     print('Числа А и B нечетные')
#
# Напишите программу для определения того, является ли данное время суток утром.
# Выведите соответствующее сообщение. Утром считается временной промежуток
# с 6 часов включительно и до 12 часов не включительно.
# hour = 7
# if 6 <= hour < 12:
#     print('Morning')
# условие проверки принадлежности точки к координатной плоскости.
# x = -1
# y = -1
#
# if x < 0 and y > 0:
#     print('I')
# if x > 0 and y > 0:
#     print('II')
# if x > 0 and y < 0:
#     print('III')
# if x < 0 and y < 0:
#     print('IV')
# speed = -11119
# def get_wind_class(speed):
#     if 1 <= speed <= 4:
#         return 'weak [1]'
#     elif 5 <= speed <= 10:
#         return 'moderate [2]'
#     elif 11 <= speed <= 18:
#         return 'strong [3]'
#     elif 19 <= speed:
#         return 'hurricane [4]'
#     else:
#         return 'calm'
# print(get_wind_class(speed))

# user_database = {
#     'user': 'password',
#     'iseedeadpeople': 'greedisgood',
#     'hesoyam': 'tgm'
# }
#
# username = 'user1'
# password = '0123'
# def check_user(username, password):
#     if username in user_database:
#         if user_database['user'] == password:
#             return True
#         else:
#             return False
#     else:
#         return False
# print(check_user(username, password))
#
# Тернарный условный оператор
# result = a if a > b else b
#
# Задание 18.5.5
# Запишите условие, которое является истинным,
# когда только одно из чисел А, В и С меньше 45.
# Иногда проще записать все условия и не пытаться упростить их.
#
# A = 44
# B = 45
# C = 45
#
# def funk1(A, B, C):
#     if A < 45 and B >= 45 and C >= 45 \
#             or B < 45 and A >= 45 and C >= 45 \
#             or C < 45 and B >= 45 and A >= 45:
#         return True
#     else:
#         return False
# print(funk1(A, B, C))
#
# Задание 18.5.6
# Запишите логическое выражение, которое определяет,
# что число А не принадлежит интервалу от -10 до -1
# или интервалу от 2 до 15.
#
# A = -5
# def interval(A):
#     if -10 <= A <= -1:
#         return 'In -10 to -1'
#     elif 2 <= A <= 15:
#         return 'In 2 to 15'
#     else:
#         return 'No one'
# print(interval(A))
#
# A = int(input('Введите число\n'))
# if not (-10 <= A <= -1 or 2 <= A <= 15):
#     print("Число не принадлежит интервалу")
# else:
#     print("Число принадлежит интервалу")
#
# Задание 18.5.7
# Дано двузначное число. Определите, входит ли в него цифра 5.
# Попробуйте решить задачу с использованием целочисленного деления и деления с остатком.

# Задание 18.5.8
# Проверьте, все ли элементы в списке являются уникальными.
#
# a = ['sd', 2, 'g', 0, 't4']
# print(len(set(a)) == len(a))

# Задание 18.5.9
# Дано натуральное восьмизначное число. Выясните, является ли оно палиндромом
# (читается одинаково слева направо и справа налево).
#
# a = (input('Vvedite XXXXXXXX chislo: '))
# b = a[::-1]
# print(a == b)
#
# num = 12345678
# print(str(num) == str(num)[::-1])
# some_var = (2,)
# if some_var is None:
#     print("NoneType")
# else:
#     print(type(some_var))
#
# a = '' # пустая строка
# b = a or 1
# print(b)

# a = "foo"
# b = "bar"
# print(1 and a or b)
# a = False
# b = False
# if a and b:
#     print("Обе переменные истинные")
#     print(a,b)
# elif a or b:
#     print("Одна из переменных истинная")
#     print(a or b)
# else:
#     print('Обе ложные')
#     print(a, b)

# Представим, что на вход нашей программы подается число.
# А мы хотим проверить, является ли оно целым, находится ли
# в определенном промежутке (например от 100 до 999 включительно),
# да еще и делится ли на 2 и 3 одновременно. Очень много условий.
# И такое случается в реальных проектах.
# a = int(input())
# if type(a) == int:
#     if 100 <= a <= 999:
#         if a % 2 == 0:
#             if a % 3 == 0:
#                 print('ДА, ебать')
# if type(a) == int and 100 <= a <= 999 and a % 2 == 0 and a % 3 == 0:
#     print('yes')
#
# Функция all([ ]) возвращает True, если все элементы списка являются истинными.
# А что если нужно, чтобы был хотя бы один истинный?
# Тогда на помощь приходит функция any([ ]). Ее работа аналогична рассмотренному выше примеру.

# a =  int(input())
# if all([type(a) == int,
#         100 <= a <= 999,
#         a % 2 == 0,
#         a % 3 == 0]):
#     print('DA')

