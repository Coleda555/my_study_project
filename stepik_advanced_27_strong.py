"""
Магический квадрат 🌶️
Магическим квадратом порядка nn называется квадратная таблица размера n \times nn×n, составленная из всех чисел 1, 2, 3,
 \ldots, n^21,2,3,…,n
2
  так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. Напишите программу,
  которая проверяет, является ли заданная квадратная матрица магическим квадратом.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы: nn
строк, по nn чисел в каждой, разделённые пробелами.

Формат выходных данных
Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.

Тестовые данные 🟢
Sample Input 1:

3
8 1 6
3 5 7
4 9 2
Sample Output 1:

YES
Sample Input 2:

3
8 2 6
3 5 7
4 9 1
Sample Output 2:

NO
Sample Input 3:

3
4 9 2
3 5 7
8 1 6
Sample Output 3:

YES
"""

n = int(input())


def checking_correct_matrix(n):
    matrix = []

    for _ in range(n):
        matrix.append([int(num) for num in input().split()])

    numbers = [i for i in range(1, n * n + 1)]

    for r in range(n):
        for c in range(n):
            if matrix[r][c] in numbers:
                numbers.remove(matrix[r][c])
            else:
                return "NO"

    amount_main_diag = 0
    amount_secondary_diag = 0
    amount_rows = 0
    amount_cows = 0

    for i in range(n):
        amount_main_diag += matrix[i][i]
        amount_secondary_diag += matrix[i][n - 1 - i]

    if amount_main_diag != amount_secondary_diag:
        return "NO"

    for r in range(n):
        for c in range(n):
            amount_rows += matrix[r][c]
            amount_cows += matrix[c][r]
        if amount_main_diag != amount_rows or amount_main_diag != amount_cows:
            return "NO"
        amount_cows = 0
        amount_rows = 0
    return "YES"


print(checking_correct_matrix(n))