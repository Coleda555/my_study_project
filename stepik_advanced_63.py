"""
Упорядоченные дроби
На вход программе подается натуральное число nn. Напишите программу, которая выводит в порядке возрастания все
несократимые дроби, заключённые между 00 и 11, знаменатель которых не превосходит nn.

Формат входных данных
На вход программе подается натуральное число n, \, n > 1n,n>1.

Формат выходных данных
Программа должна вывести ответ на задачу.

Примечание. Возможно вам потребуется функция gcd(), которая позволяет находить наибольший общий делитель (НОД) двух
чисел. Функция реализована в модуле math.

Тестовые данные 🟢
Sample Input 1:

5
Sample Output 1:

1/5
1/4
1/3
2/5
1/2
3/5
2/3
3/4
4/5
Sample Input 2:

4
Sample Output 2:

1/4
1/3
1/2
2/3
3/4
Sample Input 3:

3
Sample Output 3:

1/3
1/2
2/3
"""
from fractions import Fraction

n = int(input())
numbers = set()
check_numbres = [num for num in range(1, n + 1)]
for i in range(1, n):
    for j in range(1, n + 1):
        num = Fraction(i, j)
        if num not in check_numbres and num.numerator < num.denominator:
            numbers.add(num)
print(*sorted(numbers), sep='\n')
