# Задача: вывести в консоль элементы списка
# a = [1, 2, 3, 4]
#
# def print_list (a):
#     if len(a) != 0:
#         first_elem = a[0]
#         list_tail = a[1:]
#         print(first_elem)
#         print_list(list_tail)
# print_list(a)

# Задача: поиск максимума в списке
# a = [1, 2, 3, 4]
#
#
# def custom_max(a):
#     if len(a) == 1:
#         return a[0]
#
#     first_elem = a[0]
#     tail = a[1:]
#     tail_max = custom_max(tail)
#
#     if first_elem > tail_max:
#         return first_elem
#     else:
#         return tail_max
# print(custom_max(a))

#Задача: подсчет суммы цифр в числе
# Variant 1
# a = input('Vvedite chislo: ')
# v = [int(x) for x in str(a)]
# print ('summa: ', sum(v))

# Variant 2
# b = 123
# print(b)
#
#
# def sum_digit(b):
#     if b == 0:
#         return 0
#     last_digit = b % 10
#     tail = b // 10
#     tail_sum = sum_digit(tail)
#     return last_digit + tail_sum
# print(sum_digit(b))

# Задача: развернуть строку
# Вариант 1
# stroka = "abc"
# print(stroka[::-1])
#Вариант 2
#
#
# def rev(stroka):
#     if len(stroka) <= 1:
#         return stroka
#     return rev(stroka[1:]) + stroka[0]
# print(rev(stroka))

# Задача: числа фибоначчи
# def fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# print(fib(7))

# Использование функции
# import math
#
# print(math.sin(math.pi/2))

