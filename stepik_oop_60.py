"""
Подвиг 9. Объявите в программе класс Triangle, объекты которого создаются командой:

tr = Triangle(a, b, c)
где a, b, c - длины сторон треугольника (любые положительные числа). В каждом объекте класса Triangle должны
формироваться локальные атрибуты _a, _b, _c с соответствующими значениями.

Если в качестве хотя бы одной величины a, b, c передается не числовое значение, или меньше либо равно нулю, то должно
генерироваться исключение командой:

raise TypeError('стороны треугольника должны быть положительными числами')
Если из переданных значений a, b, c нельзя составить треугольник (условие: каждая сторона должна быть меньше суммы двух
других), то генерировать исключение командой:

raise ValueError('из указанных длин сторон нельзя составить треугольник')
Затем, на основе следующего набора данных:

input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
необходимо сформировать объекты класса Triangle, но только в том случае, если не возникло никаких исключений. Все
созданные объекты представить в виде списка с именем lst_tr.
"""


class Triangle():
    def __init__(self, a, b, c):
        if Triangle.check_side(a):
            self._a = a
        if Triangle.check_side(b):
            self._b = b
        if Triangle.check_side(c):
            self._c = c
        if not Triangle.check_triangle(self._a, self._b, self._c):
            raise ValueError('из указанных длин сторон нельзя составить треугольник')

    @staticmethod
    def check_side(value):
        if type(value) in (int, float) and value > 0:
            return value
        else:
            raise TypeError('стороны треугольника должны быть положительными числами')

    @staticmethod
    def check_triangle(a, b, c):
        return a < b + c and b < a + c and c < a + b


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
lst_tr = []
for data in input_data:
    try:
        lst_tr.append(Triangle(*data))
    except (TypeError, ValueError):
        pass

print(lst_tr)
