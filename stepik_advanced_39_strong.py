"""
Умножение матриц 🌶️
Напишите программу, которая перемножает две матрицы.

Формат входных данных
На вход программе подаются два натуральных числа n и m — количество строк и столбцов в первой матрице, затем элементы
 первой матрицы, затем пустая строка. Далее следуют числа m и k — количество строк и столбцов второй матрицы затем
  элементы второй матрицы.

Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.

Тестовые данные 🟢
Sample Input 1:

2 2
1 2
3 2

2 2
3 2
1 1
Sample Output 1:

5 4
11 8
Sample Input 2:

3 2
2 5
6 7
1 8

2 3
1 2 1
0 1 0
Sample Output 2:

2 9 2
6 19 6
1 10 1
Sample Input 3:

3 3
2 4 6
1 3 5
0 4 8

3 3
6 3 1
9 6 3
0 2 0
Sample Output 3:

48 42 14
33 31 10
36 40 12
"""

size_n_m = input().split()
n, m = int(size_n_m[0]), int(size_n_m[1])

matrix_a = []
matrix_b = []
matrix_c = []

for _ in range(n):
    matrix_a.append([int(num) for num in input().split()])

input()
size_m_k = input().split()
m, k = int(size_m_k[0]), int(size_m_k[1])

for _ in range(m):
    matrix_b.append([int(num) for num in input().split()])

for _ in range(n):
    matrix_c.append([0 for _ in range(k)])

for i in range(n):
    for j in range(k):
        num = 0
        for r in range(m):
            num += matrix_a[i][r] * matrix_b[r][j]
        matrix_c[i][j] = num

for r in range(n):
    for c in range(k):
        print(matrix_c[r][c], end=' ')
    print()