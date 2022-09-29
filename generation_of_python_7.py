'''
Переворатор
Дана последовательность натуральных чисел от 1 до n. Напишите программу, которая сначала располагает в обратном
 порядке часть элементов этой последовательности от элемента с номером X до элемента с номером Y а затем от элемента
 с номером A до элемента с номером B.

Формат входных данных
На вход программе подаются 5 натуральных чисел, разделенных пробелом: n, \, X, \, Y, \, A, \, B \,

Формат выходных данных
Программа должна сформировать последовательность чисел, согласно условию задачи, и вывести их, разделяя пробелом.

Примечание 1. Нумерация членов последовательности начинается с единицы.

Примечание 2. Рассмотрим первый тест, в котором n=9, X=2, Y=5, A=6, B=9. Запишем последовательность
от 1 до 9:
1, 2, 3, 4 , 5, 6, 7, 8, 9


Перевернем в этой последовательности сначала элементы со 2 по 5 (2, 3, 4, 5), затем с 6 по 9 (6, 7, 8, 9).
Получим искомую последовательность:
1, 5, 4, 3, 2, 9, 8, 7, 6

'''


input_num = [int(num) for num in input().split()]
result = [num for num in range(1, input_num[0] + 1)]
y = input_num[2]
b = input_num[4] - 1
for i in range(input_num[1] - 1, input_num[2]):
    result[i] = y
    y -= 1
result_copy = result.copy()
for i in range(input_num[3] - 1, input_num[4]):
    result[i] = result_copy[b]
    b -= 1
print(*result)