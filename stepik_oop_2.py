"""
Подвиг 5. Объявите класс TriangleChecker, объекты которого можно было бы создавать командой:

tr = TriangleChecker(a, b, c)
Здесь a, b, c - длины сторон треугольника.

В классе TriangleChecker необходимо объявить метод is_triangle(), который бы возвращал следующие коды:

1 - если хотя бы одна сторона не число (не float или int) или хотя бы одно число меньше или равно нулю;
2 - указанные числа a, b, c не могут являться длинами сторон треугольника;
3 - стороны a, b, c образуют треугольник.

Проверку параметров a, b, c проводить именно в таком порядке.

Прочитайте из входного потока строку, содержащую три числа, разделенных пробелами, командой:

a, b, c = map(int, input().split())
Затем, создайте объект tr класса TriangleChecker и передайте ему прочитанные значения a, b, c. Вызовите метод
is_triangle() из объекта tr и выведите результат на экран (код, который она вернет).

Sample Input:

3 4 5
Sample Output:

3
"""


class TriangleChecker:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        sides = (self.a, self.b, self.c)
        result = set()
        flag = True
        for item in sides:
            if type(item) == float or type(item) == int:
                if item <= 0:
                    result.add(1)
                    flag = False
            else:
                result.add(1)
                flag = False

        if flag:
            three_sides = sum(sides)
            for side in sides:
                if side >= three_sides - side:
                    result.add(2)
            if 2 not in result:
                result.add(3)
        return result.pop()


a, b, c = map(lambda x: x, input().split())
# a, b, c = map(lambda x: int(x), input().split()) для проверки сторон треугольника
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
