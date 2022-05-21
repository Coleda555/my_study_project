"""
Упаковка дубликатов 🌶️
На вход программе подается строка текста, содержащая символы. Напишите программу, которая упаковывает последовательности одинаковых символов заданной строки в подсписки.

Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела.

Формат выходных данных
Программа должна вывести указанный вложенный список.

Тестовые данные 🟢
Sample Input 1:

a b c d
Sample Output 1:

[['a'], ['b'], ['c'], ['d']]
Sample Input 2:

w w w o r l d g g g g r e a t t e c c h e m g g p w w
Sample Output 2:

[['w', 'w', 'w'], ['o'], ['r'], ['l'], ['d'], ['g', 'g', 'g', 'g'], ['r'], ['e'], ['a'], ['t', 't'], ['e'], ['c', 'c'],
['h'], ['e'], ['m'], ['g', 'g'], ['p'], ['w', 'w']]
Sample Input 3:

g i v e t h h i i s m a a a n a g u u n
Sample Output 3:

[['g'], ['i'], ['v'], ['e'], ['t'], ['h', 'h'], ['i', 'i'], ['s'], ['m'], ['a', 'a', 'a'], ['n'], ['a'], ['g'],
['u', 'u'], ['n']]
"""

# input_list_string = input().split()
input_list_string = 'g i v e t h h i i s m a a a n a g u u n'.split()
print(input_list_string)
output_list = []
index_out = 0
if len(input_list_string) > 1:
    output_list.append([input_list_string[0]])
    for i in range(1, len(input_list_string)):
        if input_list_string[i] == input_list_string[i - 1]:
            output_list[index_out].append(input_list_string[i])
        else:
            output_list.append([input_list_string[i]])
            index_out += 1
print(output_list)
