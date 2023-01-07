myFile = open('filename.txt', 'rt', encoding="utf8")
# print(myFile.read())
# print(myFile.read(10))
# print(myFile.readline())
# print(myFile.readline(10))

# print(myFile.readlines())
#
# for line in myFile:
#     print(line)
#
# miFile = open('fillname.txt', 'w')
# #
# miFile.write('HUI')
# print('xxx', file=miFile)
# print('ololo', file=miFile)
# miFile.write('HUI')
#
# with open('filename.txt') as myFile:
#     for line in myFile:
#         print(line)
#
# Закодировать строку сдвигом на определенное количество символов
# alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# alphaUP = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# number = int(input('vvedi chislo zaebal: '))
# summary = ''
# def changeChar(char):
#     if char in alpha:
#         return alpha[(alpha.index(char) + number) % len(alpha)]
#     if char in alphaUP:
#         return alphaUP[(alphaUP.index(char) + number) % len(alphaUP)]
#     else:
#         return char
#
# with open('zakod.txt', encoding='utf8') as myFile:
#     for line in myFile:
#         for char in line:
#             summary += changeChar(char)
#
# print(summary)
#
# with open('fillname.txt', 'w', encoding='utf8') as myFile:
#     myFile.write(summary)

