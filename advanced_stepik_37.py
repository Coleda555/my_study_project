"""
Заполнение спиралью 😈😈
На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером n \times
mn×m заполнив её "спиралью" в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии образцом.

Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 33 символа на каждый элемент. Для этого
используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇

Тестовые данные 🟢
Sample Input 1:

4 5
Sample Output 1:

1  2  3  4  5
14 15 16 17 6
13 20 19 18 7
12 11 10 9  8
Sample Input 2:

1 6
Sample Output 2:

1  2  3  4  5  6
Sample Input 3:

3 3
Sample Output 3:

1  2  3
8  9  4
7  6  5
"""

size = input().split()
n, m = int(size[0]), int(size[1])
matrix = []
for _ in range(n):
    matrix.append([0 for _ in range(m)])


def content_spiral(matrix):
    value = 1
    step = 0
    while True:
        m = len(matrix[0])
        n = len(matrix)
        for i in range(step, m - step):
            matrix[step][i] = value
            value += 1
            if value == m * n + 1:
                return matrix
        for i in range(step + 1, n - step):
            matrix[i][m - step - 1] = value
            value += 1
            if value == m * n + 1:
                return matrix
        for i in range(m - step - 2, step - 1, -1):
            matrix[n - step - 1][i] = value
            value += 1
            if value == m * n + 1:
                return matrix
        for i in range(n - step - 2, step, -1):
            matrix[i][step] = value
            value += 1
            if value == m * n + 1:
                return matrix
        step += 1


matrix = content_spiral(matrix)
for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end=' ')
    print()
