"""
Подвиг 8. Объявите класс с именем Rect (прямоугольник), объекты которого создаются командой:

r = Rect(x, y, width, height)
где x, y - координаты верхнего левого угла (любые числа); width, height - ширина и высота прямоугольника (положительные
числа).

В каждом объекте класса Rect должны формироваться локальные атрибуты с именами: _x, _y, _width, _height и
соответствующими значениями. Если переданные аргументы x, y (не числа) и width, height не положительные числа, то
генерировать исключение командой:

raise ValueError('некорректные координаты и параметры прямоугольника')
В классе Rect реализовать метод:

def is_collision(self, rect): ...

который проверяет пересечение текущего прямоугольника с другим (с объектом rect). Если прямоугольники пересекаются, то
должно генерироваться исключение командой:

raise TypeError('прямоугольники пересекаются')
Сформировать в программе несколько объектов класса Rect со следующими значениями:

0; 0; 5; 3
6; 0; 3; 5
3; 2; 4; 4
0; 8; 8; 1

Сохранить их в списке lst_rect. На основе списка lst_rect сформировать еще один список lst_not_collision, в котором
должны быть объекты rect не пересекающиеся ни с какими другими объектами в списке lst_rect.

P.S. В программе требуется объявить только класс и списки. На экран выводить ничего не нужно.

Подсказка. Для определения пересечения двух прямоугольников, у которых стороны параллельны осям координат (как в этом
подвиге) достаточно проверить, что верхняя грань первого прямоугольника находится ниже нижней грани второго, или нижняя
грань первого прямоугольника выше верхней грани второго. И то же самое для вертикальных граней.
"""


class Rect:
    def __init__(self, x, y, width, height):
        self._x = self.validator_number(x)
        self._y = self.validator_number(y)
        self._width = self.validator_positive(self.validator_number(width))
        self._height = self.validator_positive(self.validator_number(height))



    def validator_number(self, value):
        if type(value) in (int, float):
            return value
        else:
            raise ValueError('некорректные координаты и параметры прямоугольника')

    def validator_positive(self, value):
        if  value > 0:
            return value
        else:
            raise ValueError('некорректные координаты и параметры прямоугольника')

    def is_collision(self, rect):
        if not isinstance(rect, Rect):
            raise TypeError ("Объект не класса React")
        if not(self._x + self._width < rect._x or rect._x + rect._width < self._x or self._y + self._height < rect._y
               or rect._y + rect._height < self._y):
            raise TypeError('прямоугольники пересекаются')


lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]
lst_not_collision = []
for i in lst_rect:
    result = []
    for j in lst_rect:
        if i is not j:
            try:
                i.is_collision(j)
            except TypeError:
                result.append(False)
            else:
                result.append(True)
    if all(result):
        lst_not_collision.append(i)

print(lst_not_collision)

