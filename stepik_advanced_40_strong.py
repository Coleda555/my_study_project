"""
Возведение матрицы в степень 🌶️
Напишите программу, которая возводит квадратную матрицу в m-ую степень.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы, затем
натуральное число m.

Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.

Тестовые данные 🟢
Sample Input 1:

3
1 2 3
4 5 6
7 8 9
2
Sample Output 1:

30 36 42
66 81 96
102 126 150
Sample Input 2:

3
1 2 1
3 3 3
1 2 1
5
Sample Output 2:

1666 2222 1666
3333 4443 3333
1666 2222 1666
Sample Input 3:

5
1 2 1 1 2
3 3 3 3 3
1 2 1 1 2
3 3 3 3 3
1 2 1 1 2
3
Sample Output 3:

133 176 133 133 176
279 369 279 279 369
133 176 133 133 176
279 369 279 279 369
133 176 133 133 176
"""


def print_matrix(matrix):
    for r in range(n):
        for c in range(n):
            print(matrix[r][c], end=' ')
        print()


n = int(input())
matrix_a = []
for _ in range(n):
    matrix_a.append([int(num) for num in input().split()])
m = int(input())

matrix_m = []
for _ in range(n):
    matrix_m.append([0 for _ in range(n)])

for i in range(n):
    for j in range(n):
        matrix_m[i][j] = matrix_a[i][j]

matrix_c = []
for _ in range(n):
    matrix_c.append([0 for _ in range(n)])

for _ in range(m - 1):
    for i in range(n):
        for j in range(n):
            num = 0
            for r in range(n):
                num += matrix_m[i][r] * matrix_a[r][j]
            matrix_c[i][j] = num
    matrix_m = matrix_c
    print_matrix(matrix_m)

'''for r in range(n):
    for c in range(n):
        print(matrix_m[r][c], end=' ')
    print()'''
