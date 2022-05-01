"""
Повторяйповторяйповторяй
Напишите программу, которая определяет, на какое максимальное количество одинаковых подстрок можно разбить данную строку
 так, чтобы все элементы строки были задействованы.

Формат входных данных
На вход программе подается одна строка, состоящая из строчных латинских букв., длина которой не превышает 400000
 символов.

Формат выходных данных
Программа должна вывести одно натуральное число — максимальное количество подстрок в разбиении из условия.

Примечание 1. Рассмотрим первый тест. Строку abcabcabc можно разбить на 33 одинаковые подстроки: abc, abc и abc.

Примечание 2. Рассмотрим шестой тест. Строку bebebeb можно разбить на единственную подстроку bebebeb, соответствующую
исходной. Разбиение на подстроки, например, be или beb невозможно, так как в любом случае остаются незадействованные
элементы строки.

Sample Input 1:

abcabcabc
Sample Output 1:

3
Sample Input 2:

acdc
Sample Output 2:

1
Sample Input 3:

bbbbbb
Sample Output 3:

6
Sample Input 4:

abobaboabobabo
Sample Output 4:

2
Sample Input 5:

abobaboaaabobaboaa
Sample Output 5:

2
Sample Input 6:

bebebeb
Sample Output 6:

1
"""

line = [i for i in input()]


def amount(line):
    count_twist = []
    checked = []
    counter = 1
    for char in line:
        if char not in checked:
            checked.append(char)
            count_twist.append(line.count(char))
    if len(count_twist) == 1:
        return count_twist[0]
    if count_twist.count(count_twist[0]) == len(count_twist):
        return count_twist[0]
    while True:
        for i in range(len(count_twist)):
            if count_twist[i] % 2 == 0:
                count_twist[i] = count_twist[i] % 2 == 0
            else:
                return counter
        counter += 1


print(amount(line))
