# Программа,  которая получает от пользователя имя файла,
# открывает этот файл в текущем каталоге, читает его и выводит два слова:
# наиболее часто встречающееся из тех, что имеют размер более трех символов,
# и наиболее длинное слово на английском языке.

myFile = input('Vvedite imya: ')

def changeText(text):
    for i in r'!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~':
        text = text.replace(i, '')
    return text.split()

def mostCommon(text, length = 3):
    most_common = []
    frequency = 0
    for item in text:
        if len(item) > length:
            count = text.count(item)
            if count > frequency:
                frequency = count
                most_common = [item]
            elif count == frequency:
                most_common.append(item)
    return list(set(most_common))

def mostLength(text):
    most_length = []
    frequency = 0
    alphabet = 'absdefghijklmnopqrstuvwxyzABSDEFGHIJKLMNOPQRSTUVWXYZ'
    for item in text:
        for i in item:
            if i not in alphabet:
                in_alphabet = False
            else:
                in_alphabet = True

        if in_alphabet:
            count = len(item)
            if count > frequency:
                most_length = [item]
                frequency = count
            if count == frequency:
                most_length.append(item)
    return list(set(most_length))

with open(myFile, encoding='utf8') as f:
    fileText = f.read()

fileText = changeText(fileText)
print(f'Список самых частых слов длинной более 3х символов: {mostCommon(fileText)}')
print(f'Список самых длинных английских слов: {mostLength(fileText)}')