"""
Подвиг 5. Объявите в программе класс Point, объекты которого должны создаваться командами:

pt = Point()
pt = Point(x, y)
где x, y - произвольные числа (координаты точки).

В каждом объекте класса Point должны формироваться локальные атрибуты _x, _y с соответствующими значениями. Если
аргументы не указываются (первая команда), то _x = 0, _y = 0.

Далее, в программе вводятся два значения в одну строчку через пробел. Значениями могут быть числа, слова, булевы
величины (True/False). Необходимо прочитать эти значения из входного потока. Если оба значения являются числами, то
формировать объект pt командой:

pt = Point(x, y)
Если хотя бы одно из значений не числовое, то формировать объект pt командой:

pt = Point()
Реализовать этот функционал с помощью блоков try/except. А в блоке finally вывести на экран сообщение в формате (без
кавычек):

"Point: x = <значение x>, y = <значение y>"
"""


class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y


lst_in = input().split()


def check(lst_in):
    result = []
    for value in lst_in:
        try:
            value = int(value)
            result.append(value)
        except:
            try:
                value = float(value)
                result.append(value)
            except:
                return Point()
    return Point(*result)

pt = check(lst_in)

print(f"Point: x = {pt.get_x()}, y = {pt.get_y()}")
