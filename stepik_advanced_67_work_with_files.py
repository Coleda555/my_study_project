"""
Конкатенация файлов 🌶️
На вход программе подается натуральное число nn и nn строк с названиями файлов. Напишите программу, которая создает файл
 output.txt и выводит в него содержимое всех файлов с указанными именами, не меняя их порядка.

Формат входных данных
На вход программе подается натуральное число nn и nn строк названий существующих файлов.

Формат выходных данных
Программа должна создать файл с именем output.txt в соответствии с условием задачи.

Примечание. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.
"""
n = int(input())
files = [input() for _ in range(n)]
print(files)
text = []


def read_file(name: str):
    with open(name, 'r', encoding='utf-8') as file:
        return file.readlines()

for name in files:
    text += read_file(name)
    text.append('\n')

print(text)

with open('output.txt', 'w', encoding='utf-8') as output:
    output.writelines(text)