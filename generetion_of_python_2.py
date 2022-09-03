"""
Функция convert()
Реализуйте функцию convert(), которая принимает один аргумент:

string — произвольная строка
Функция должна возвращать строку string:

полностью в нижнем регистре, если букв в нижнем регистре в этой строке больше
полностью в верхнем регистре, если букв в верхнем регистре в этой строке больше
полностью в нижнем регистре, если количество букв в верхнем и нижнем регистрах в этой строке совпадает
Примечание 1. Символы строки, не являющиеся буквами, следует игнорировать.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию convert(), но не код,
вызывающий ее.
"""


import string as s


def convert(string: str):
    count_upper = 0
    count_lower = 0
    for letter in string:
        if letter in s.ascii_uppercase:
            count_upper += 1
        if letter in s.ascii_lowercase:
            count_lower += 1

    if count_lower >= count_upper:
        return string.lower()
    else:
        return string.upper()


print(convert('BEEgeek'))
print(convert('pyTHON'))
print(convert('pi31415!'))
