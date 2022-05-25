"""
Максимальный в области 2
Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.



Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы.

Формат выходных данных
Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.

Примечание. Элементы побочной диагонали также учитываются.

Тестовые данные 🟢
Sample Input 1:

3
1 4 5
6 7 8
1 1 6
Sample Output 1:

8
Sample Input 2:

4
0 1 4 6
0 0 2 5
0 0 0 7
0 0 0 0
Sample Output 2:

7
Sample Input 3:

2
6 0
7 9
Sample Output 3:

9
"""
n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(num) for num in input().split()])
numbers = []
for i in range(n):
    for j in range(n):
        if i <= j and i >= n - 1 -j:
            numbers.append(matrix[i][j])
        elif i >= j and i >= n - 1 -j:
            numbers.append(matrix[i][j])

print(max(numbers))