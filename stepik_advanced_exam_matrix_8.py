"""
Диагонали параллельные главной
На вход программе подается натуральное число nn. Напишите программу, которая создает матрицу размером n \times nn×n и заполняет её по следующему правилу:

на главной диагонали на месте каждого элемента должно стоять число 00;
на двух диагоналях, прилегающих к главной, число 11;
на следующих двух диагоналях число 22, и т.д.
Формат входных данных
На вход программе подается натуральное число nn — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии с условием задачи.

Тестовые данные 🟢
Sample Input 1:

5
Sample Output 1:

0 1 2 3 4
1 0 1 2 3
2 1 0 1 2
3 2 1 0 1
4 3 2 1 0
Sample Input 2:

2
Sample Output 2:

0 1
1 0
Sample Input 3:

3
Sample Output 3:

0 1 2
1 0 1
2 1 0
"""
n = int(input())
matrix = []
for _ in range(n):
    matrix.append([0 for _ in range(n)])
counter = 0
while counter < n:
    for i in range(n):
        for j in range(n):
            if i - counter == j:
                matrix[i][j] = counter
            elif j - counter == i:
                matrix[i][j] = counter
    counter += 1

for r in range(n):
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()