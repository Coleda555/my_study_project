"""
Латинский квадрат 🌶️
Латинским квадратом порядка nn называется квадратная матрица размером n \times nn×n, каждая строка и каждый столбец
которой содержат все числа от 11 до nn. Напишите программу, которая проверяет, является ли заданная квадратная матрица
латинским квадратом.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы: nn
строк, по nn чисел в каждой, разделённые пробелами.

Формат выходных данных
Программа должна вывести слово YES, если матрица является латинским квадратом, и слово NO, если не является.

Тестовые данные 🟢
Sample Input 1:

4
2 3 4 1
3 4 1 2
4 1 2 3
1 2 3 4
Sample Output 1:

YES
Sample Input 2:

3
1 2 3
3 2 1
2 3 4
Sample Output 2:

NO
"""
n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(num) for num in input().split()])
numbers = [i for i in range(1, n + 1)]
flag = True
check_rows = []
check_column = []
for r in range(n):
    for c in range(n):
        if matrix[r][c] not in check_rows and matrix[r][c] in numbers:
            check_rows.append(matrix[r][c])
        else:
            flag = False
        if matrix[c][r] not in check_column and matrix[c][r] in numbers:
            check_column.append(matrix[c][r])
        else:
            flag = False
    check_rows = []
    check_column = []
if flag:
    print("YES")
else:
    print("NO")