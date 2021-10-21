"""6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое."""

import locale

print(locale.getpreferredencoding())

file = open("test_file.txt", "w")
file.write("сетевое программирование\n")
file.write("сокет\n")
file.write("декоратор\n")

print(file.encoding)
file.close()

with open("test_file.txt", encoding='Windows-1251') as file:
    for line in file:
        print(line, end='')
