# title = input('title: ')
# author = input('author: ')
# year = input('year: ')
#
# d = {'title': title,
#      'author': author,
#      'year': int(year)}
# print(d)

# title = input()
# author = input()
# year = input()
#
# d = {'title': title,
#      'author': author,
#      'year': int(year)}
# print(d)

# L = input('Vvedi: ')
# c = list(set(L))
# print(len(c))

# name = input('vvedite: ')
# name_mod = name[0].upper() + name[1:].lower()
# print('Hello, ', name_mod)

# a = set(input("Введите первую строку: "))
# b = set(input("Введите вторую строку: "))
#
# # a_set, b_set = set(a), set(b) # используем множественное присваивание
# a_and_b = b.symmetric_difference(a)
#
# print(a_and_b)

# L = ['a', 'b', 'c']
# print(id(L))
#
# L.append('d')
# print(id(L))

# a = 5
# b = 3+2
#
# print(int(id(a))-int(id(b)))

# shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
# list_id_before = id(shopping_center[-1])
# print(list_id_before)
#
# shopping_center[-1].append("Uniqlo")
# list_id_after = id(shopping_center[-1])
# print(list_id_after)
#
# print(list_id_before is list_id_after)