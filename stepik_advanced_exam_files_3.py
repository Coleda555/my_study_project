"""
Пропущенные комменты 🌶️
При написании собственных функций рекомендуется в комментарии описывать назначение функции, ее параметры и возвращаемое
значение. Часто программисты откладывают написание таких комментариев напоследок, а потом и вовсе забывают о них 😂.

На вход программе подается строка текста с именем текстового файла, в котором написан код на языке Python. Напишите
программу, выводящую на экран имена всех функций для которых отсутствует поясняющий комментарий. Будем считать, что
любая строка, начинающаяся со слова def и пробела, является началом определения функции. Функция содержит комментарий,
если первый символ предыдущей строки - #.

Формат входных данных
На вход программе подается строка текста, содержащая имя существующего текстового файла с кодом на языке Python.

Формат выходных данных
Программа должна вывести названия всех функций (не меняя порядка их следования в исходном файле), каждое на отдельной
строке, для которых отсутствует поясняющий комментарий. Если все функции в файле имеют поясняющий комментарий, то
следует вывести: Best Programming Team

Примечание 1. Если бы файл содержал код:

def powers(a):
    return a, a**2, a**3

# функция вычисляет сумму всех переданных чисел
def sum_all(*args):
    return sum(args)

def matrix():
    pass

# функция возвращает количество переданных аргументов
def count_args(*args):
    return len(args)

def mean(*args):
    total = 0.0
    count = 0
    for i in args:
        if type(i) in (int, float):
            total += i
            count += 1
    if count == 0:
        return 0.0
    else:
        return total / count

def greet(name, *args):
    args = (name,) + args
    return f'Hello, {" and ".join(args)}!'

# функция вычисляет факториал переданного числа
def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
то результатом будет:

powers
matrix
mean
greet
Примечание 2. Гарантируется, что в файле есть хотя бы одна функция при этом вложенных функций в файле нет.
"""

# name = input()
name = 'code.txt'
result = []
with open(name, 'r', encoding='utf-8') as file:
    code = list(map(lambda line: line.strip(), file.readlines()))

for i in range(len(code)):
    if code[i].startswith('def '):
        if i != 0 and code[i - 1].startswith('#') == False:
            parts = code[i].split()
            result.append(parts[1].split('(')[0])
        elif i == 0:
            parts = code[i].split()
            result.append(parts[1].split('(')[0])

if len(result) != 0:
    for function in result:
        print(function)
else:
    print('Best Programming Team')
