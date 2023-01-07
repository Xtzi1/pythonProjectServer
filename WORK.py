# def linear_solve(a, b):
#     if a:
#         return b/a
#     elif not a and not b: # снова используем числа в логических выражениях
#         return "Бесконечное количество корней"
#     else:
#         return "Нет корней"
# # 2*x = 9
# print(linear_solve(2, 9))
# print(linear_solve(0,1))

#
# Квадратное уравнение
# a*x**2 + b*x + c = 0 - общий вид уравнения
# D = b**2 - 4*a*c - дискриминант
# Если D<0, то уравнение не имеет вещественных корней
# Если D=0, то уравнение имеет один корень - x = -b/(2*a)
# Если D>0, то уравнение имеет два корня
# x1 = (-b - D**0.5)/(2*a)
# x2 = (-b + D**0.5)/(2*a)
#
# P.S. D**0.5 - равносильно извлечению квадратного корня

# def D(a,b,c):
#     diskriminant = b**2 - 4*a*c
#     if diskriminant < 0:
#         return ('Нет вещественных корней')
#     elif diskriminant == 0:
#         return -b / (2*a)
#     else:
#         return (-b - diskriminant**0.5)/(2*a), (-b + diskriminant**0.5)/(2*a)
# print(D(1, 1, 1))
#
# def D(a,b,c):
#     return b**2 - 4*a*c
# def quadratic_solve(a,b,c):
#     if D(a,b,c) < 0:
#         return 'Нет корней'
#     elif D(a,b,c) == 0:
#         return -b/(2*a)
#     else:
#         return (-b-D(a,b,c)**0.5)/(2*a), (-b+D(a,b,c)**0.5)/(2*a)
# print(quadratic_solve(1, 0, -1))

# L = list(map(float, input().split()))
# M = {'a' : 1,
#      'b' : 0,
#      'c' : -1}
# print(quadratic_solve(**M))
# print(*M.values())
#

# Напишите рекурсивную функцию, находящую минимальный элемент
# списка без использование циклов и встроенной функции min().
# L = [51]
#
# def min(L):
#     if len(L) == 1:
#         return L[0]
#     return L[0] if L[0] < min(L[1:]) else min(L[1:])
#
# print(min(L))
# print('---')
#
# def min_list(L):
#     if len(L) == 1:
#         return L[0]
#     return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])
#
# print(min_list(L))

# Сейчас попробуем реализовать функцию equal(N, S), проверяющую,
# совпадает ли сумма цифр числа N с числом S. При написании программы
# следует обратить внимание на то, что, если S стала отрицательной,
# то необходимо сразу вернуть False.

# def equal(N, S):
#     if S < 0:
#         return False
#     if N < 10:
#         return N == S
#     else:
#         return (equal(N // 10, S - N % 10))
#
# print(equal(15, 6))
# #
# Теперь попробуем написать генератор для приближенного
# вычисления числа e = 2.718. Для нахождения числа, удовлетворяющего
# необходимой точности будем использовать следующий цикл:

# last = 0
# for a in e(): # e() - генератор
#     if (a - last) < 0.00000001: # ограничение на точность
#         print(a)
#         break # после достижения которого - завершаем цикл
#     else:
#         last = a # иначе - присваиваем новое значение
#
#
# def e():
#     n = 1
#
#     while True:
#         yield (1 + 1 / n) ** n
#         n += 1

iter_obj = iter("Hello!")

print(next(iter_obj))