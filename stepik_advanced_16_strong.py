"""
Разбиение на чанки 🌶️
На вход программе подаются две строки, на одной символы, на другой число nn. Из первой строки формируется список.

Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска), а возвращает список из чанков указанной длины.

Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела и число nn на отдельной строке.

Формат выходных данных
Программа должна вывести указанный вложенный список.

Примечание. Не забудьте вызвать функцию chunked(), чтобы вывести результат 😀.

Тестовые данные 🟢
Sample Input 1:

a b c d e f
2
Sample Output 1:

[['a', 'b'], ['c', 'd'], ['e', 'f']]
Sample Input 2:

a b c d e f
3
Sample Output 2:

[['a', 'b', 'c'], ['d', 'e', 'f']]
Sample Input 3:

a b c d e f
6
Sample Output 3:

[['a', 'b', 'c', 'd', 'e', 'f']]
Sample Input 4:

a b c d e f r g b
2
Sample Output 4:

[['a', 'b'], ['c', 'd'], ['e', 'f'], ['r', 'g'], ['b']]
Sample Input 5:

a b
3
Sample Output 5:

[['a', 'b']]
"""

input_string_list = input().split()
length = int(input())


def chunked(input_list, input_length):
    output_list = [[]]
    if len(input_list) > 1:
        index_out = 0

        for i in range(1, len(input_list) + 1):
            if i % input_length != 0:
                output_list[index_out].append(input_list[i - 1])
            else:
                output_list[index_out].append(input_list[i - 1])
                if i != len(input_list):
                    output_list.append([])
                    index_out += 1
        return output_list
    return []


print(chunked(input_string_list, length))
