"""
Поворот матрицы
Напишите программу, которая поворачивает квадратную матрицу чисел на 90^{\circ}90
∘
  по часовой стрелке.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы
построчно через пробел.

Формат выходных данных
Программа должна вывести результат на экран, числа должны быть разделены одним пробелом.

Тестовые данные 🟢
Sample Input 1:

3
1 2 3
4 5 6
7 8 9
Sample Output 1:

7 4 1
8 5 2
9 6 3
Sample Input 2:

4
1 9 4 2
3 8 1 5
6 7 4 6
1 9 7 8
Sample Output 2:

1 6 3 1
9 7 8 9
7 4 1 4
8 6 5 2
Sample Input 3:

2
1 2
3 4
Sample Output 3:

3 1
4 2
"""
n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(num) for num in input().split()])

matrix_output = []
for _ in range(n):
    matrix_output.append([0 for i in range(n)])

for i in range(n):
    for j in range(n):
        matrix_output[i][j] = matrix[-j - 1][i]

for r in range(n):
    for c in range(n):
        print(matrix_output[r][c], end=' ')
    print()
