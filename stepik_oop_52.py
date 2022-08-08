"""
Подвиг 10 (на повторение). Объявите базовый класс с именем ItemAttrs, который бы позволял обращаться к локальным
атрибутам объектов дочерних классов по индексу. Для этого в классе ItemAttrs нужно переопределить следующие методы:

__getitem__() - для получения значения атрибута по индексу;
__setitem__() - для изменения значения атрибута по индексу.

Объявите дочерний класс Point для представления координаты точки на плоскости. Объекты этого класса должны создаваться
командой:

pt = Point(x, y)
где x, y - целые или вещественные числа.

Пример использования классов (эти строчки в программе не писать):

pt = Point(1, 2.5)
x = pt[0]   # 1
y = pt[1]   # 2.5
pt[0] = 10
"""


class ItemAttrs:
    def __init__(self, *args):
        self.items = list(args)

    def __getitem__(self, item):
        if 0 <= item < len(self.items):
            return self.items[item]
        raise ValueError

    def __setitem__(self, key, value):
        if 0 <= key < len(self.items):
            self.items[key] = value
        else:
            raise IndexError


class Point(ItemAttrs):
    pass


pt = Point(1, 2.5)
x = pt[0]  # 1
print(x)
y = pt[1]  # 2.5
print(y)
pt[0] = 10
