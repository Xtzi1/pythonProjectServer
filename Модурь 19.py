# Напишите функцию print_2_add_2, которая будет складывать 2 и 2,
# а затем печатать этот результат. Не забудьте вызвать функцию,
# чтобы увидеть результат.
#
# def print_2_add_2():
#     return (2+2)
# print(print_2_add_2())
#
# def hw():
#     print('Hello, world')
# hw()

# Напишите функцию, которая проверяет, является ли число n делителем числа a.
# И выводит на экран соответствующее сообщение, является ли число делителем или нет.

# def delitel(a, n):
#     if a % n == 0:
#         return ('Является')
#     else:
#         return ('Не является')
# print(delitel(7, 2))
#
# Напишите функцию, которая печатает «обратную лесенку» следующего типа:
# n = 3
# ***
# **
# *
# n=4
# def lesenka(n):
#     for i in range(n+1):
#         i = n - i
#         print(i*'*')
# lesenka(n)
#
# def reverse_stair(n):
#    for i in range(n, 0, -1):
#        print("*" * i)
#
# reverse_stair(5)

# Напишите функцию, которая будет возвращать количество делителей числа а.
# Пример ввода: 5
# Пример вывода программы: 2
# def deliteli(n):
#     count = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             count += 1
#     return count
# print(deliteli(8))
# Напишите функцию, которая проверяет, является ли данная строка
# палиндромом или нет, и возвращает результат проверки. Пример:
# check_palindrome("test")  # False
# check_palindrome("Кит на море не романтик")  # True

# def check_palindrome(some_text):
#     some_text = some_text.lower()
#     some_text = some_text.replace(" ", '')
#     if some_text == some_text[::-1]:
#         return True
#     else:
#         return False
# print(check_palindrome("test"))
# print(check_palindrome("Кит на море не романтик"))
# print(check_palindrome("А роза упала на лапу Азора"))

# Давайте рассмотрим задачку и сделаем функцию сумматор,
# которая будет складывать любое количество переданных ей аргументов.
#
# def summator(*args):
#     count = 1
#     for i in args:
#         count *= i
#     return count
#
# print(summator(2,2,2))
# факториал!
# def factorial(n):
#     if n == 1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))

# fibonacci
# def fib(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     return fib(n-2) + fib(n-1)
# print(fib(10))
#
# С помощью рекурсивной функции найдите сумму чисел от 1 до n.
#
# def sum(n):
#     if n == 1:
#         return 1
#     return n + sum(n-1)
# print(sum(5))
#
# С помощью рекурсивной функции разверните строку.
# def reverse(m):
#     if len(m) == 0:
#         return ''
#     else:
#         return m[-1] + reverse(m[:-1])
# print(reverse('qwer'))

# Дано натуральное число N. Вычислите сумму его цифр.
# При решении этой задачи нельзя использовать строки,
# списки, массивы (ну и циклы, разумеется).
# def summa_chisel(N):
#     if N < 10:
#         return N
#     else:
#         return N % 10 + summa_chisel(N // 10)
# print(summa_chisel(4537))

# реализуем бесконечную последовательность чисел Фибоначчи,
# при это она будет эффективной, потому что для вычисления каждого
# следующего числа нам нужно будет хранить в памяти лишь два предыдущих значения.
# def fib():
#     a, b = 0, 1
#     yield a
#     yield b
#
#     while True:
#         a, b = b, a + b
#         yield b
# for num in fib():
#    print(num)

# Создайте функцию-генератор, возвращающую бесконечную последовательность
# натуральных чисел. По умолчанию, она начинается с единицы и шагом 1,
# но пользователь может указать любой шаг и любое число в качестве аргумента
# функции, с которого будет начинаться последовательность.
# def beskonechnost(num=1, step=1):
#     counter = num
#     while True:
#         yield counter
#         counter += step
# for num in beskonechnost():
#    print(num)

# Создайте генератор цикла, то есть в функцию на входе будет передаваться
# массив, например, [1, 2, 3], генератор будет вечно работать возвращая 1 2 3 1 2 3… и так далее.
#
# def generator(num):
#     counter = num
#     while True:
#         yield counter
#         counter += num
# for num in generator(1, 2, 3):
#     print(num)
#
# def repeat_list(list_):
#    list_values = list_.copy()
#    while True:
#        value = list_values.pop(0)
#        list_values.append(value)
#        yield value
# for i in repeat_list([1, 2, 3]):
#    print(i)
#
# Сделаем функцию, которая будет возвращать функцию, всегда прибавляющую одно и тоже число x:
# def make_adder(x):
#     def adder(n):
#         return n + x
#     return adder
# # add_5 = make_adder(7)
# # print(add_5(10))
# add_10 = make_adder(10)
# print(add_10(6))

# def my_func():
#     print('я оборачиваемая функция!')
#     return 0
# print(my_func())
#
# def decorator(func_to_decorate):
#     def obertka():
#         print('я выполняюсь до основного вызова')
#         result = func_to_decorate()
#         print('а я после')
#         return result
#     return obertka
#
# decorated_func = decorator(my_func)
# print(decorated_func())
#
# import time
#
# N = 100
#
#
# def decorator_time(fn):
#    def wrapper():
#        t0 = time.time()
#        result = fn()
#        dt = time.time() - t0
#        return dt
#    return wrapper
#
#
# def pow_2():
#    return 10000000 ** 2
#
#
# def in_build_pow():
#    return pow(10000000, 2)
#
#
# pow_2 = decorator_time(pow_2)
# in_build_pow = decorator_time(in_build_pow)
#
# mean_pow_2 = 0
# mean_in_build_pow = 0
# for _ in range(N):
#    mean_pow_2 += pow_2()
#    mean_in_build_pow += in_build_pow()
#
# print(f"Функция {pow_2} выполнялась {N} раз. Среднее время: {mean_pow_2 / N:.10f}")
# print(f"Функция {in_build_pow} выполнялась {N} раз. Среднее время: {mean_in_build_pow / 100:.10f}")

#Вот универсальный шаблон для декоратора:
# def my_decorator(fn):
#     print("Этот код будет выведен один раз в момент декорирования функции")
#     def wrapper(*args, **kwargs):
#         print('Этот код будет выполняться перед каждым вызовом функции')
#         result = fn(*args, **kwargs)
#         print('Этот код будет выполняться после каждого вызова функции')
#         return result
#     return wrapper
# Напишите декоратор, который будет подсчитывать количество вызовов
# декорируемой функции. Для хранения переменной, содержащей количество
# вызовов, используйте nonlocal область декоратора.
# count = 0
# def my_decorator(fn):
#     print("Этот код будет выведен один раз в момент декорирования функции")
#     count = 0
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         print('Этот код будет выполняться перед каждым вызовом функции')
#         result = fn(*args, **kwargs)
#         count += 1
#         print(f'Функция {fn} была вызвана {count} раз')
#         return result
#     return wrapper
#
# @my_decorator
# def say_word(word):
#     print(word)
#
# say_word('ХУЙ')
#
# say_word('ХУЙ')
#
# say_word('ХУЙ')

