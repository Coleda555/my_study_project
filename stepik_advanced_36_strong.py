"""
Заполнение диагоналями 🌶️
На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером n \times mn×m заполнив её "диагоналями" в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом.

Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 33 символа на каждый элемент. Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇

Тестовые данные 🟢
Sample Input 1:

3 5
Sample Output 1:

1  2  4  7  10
3  5  8  11 13
6  9  12 14 15
Sample Input 2:

3 4
Sample Output 2:

1  2  4  7
3  5  8  10
6  9  11 12
Sample Input 3:

2 2
Sample Output 3:

1  2
3  4
Sample Input 4:

8 1
Sample Output 4:

1
2
3
4
5
6
7
8
Sample Input 5:

8 2
Sample Output 5:

1  2
3  4
5  6
7  8
9  10
11 12
13 14
15 16
"""

size = input().split()
n, m = int(size[0]), int(size[1])
matrix = []
for _ in range(n):
    matrix.append([0 for _ in range(m)])
step = 0
value = 1
while step != m * n + 1:
    for i in range(n):
        for j in range(m):
            if i + j == step:
                matrix[i][j] = value
                value += 1
    step += 1

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end=' ')
    print()
