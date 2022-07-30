class Vector:
    def __init__(self, *args):
        self.coords = args

    def get_coords(self):
        return self.coords

    @staticmethod
    def __addition(tuple1, tuple2):
        if len(tuple1) != len(tuple2):
            raise TypeError('размерности векторов не совпадают')
        return tuple(map(lambda i, j: i + j, tuple1, tuple2))

    @staticmethod
    def __subtraction(tuple1, tuple2):
        if len(tuple1) != len(tuple2):
            raise TypeError('размерности векторов не совпадают')
        return tuple(map(lambda i, j: i - j, tuple1, tuple2))

    def __sub__(self, other):
        other_coord = None
        if isinstance(other, tuple):
            other_coord = other
        elif type(other) in (Vector, VectorInt):
            other_coord = other.get_coords()

        result = self.__subtraction(self.coords, other_coord)
        print(result)
        for coord in result:
            if type(coord) == float:
                return Vector(*result)
        return VectorInt(*result)

    def __add__(self, other):
        other_coord = None
        if isinstance(other, tuple):
            other_coord = other
        elif type(other) in (Vector, VectorInt):
            other_coord = other.get_coords()

        result = self.__addition(self.coords, other_coord)
        print(result)
        for coord in result:
            if type(coord) == float:
                return Vector(*result)
        return VectorInt(*result)


class VectorInt(Vector):
    def __init__(self, *args):
        for coord in args:
            if type(coord) != int:
                raise ValueError('координаты должны быть целыми числами')
        super().__init__(*args)


v7 = VectorInt(1, 2, 3, 4)
print(v7.get_coords())
#v2 = VectorInt(1, 0.2, 3,
               #4)  # ошибка: генерируется исключение raise ValueError('координаты должны быть целыми числами')
#v3 = Vector(2, 3, 4, 5)

#v4 = v1 + v2  # v1 - объект класса VectorInt
#v5 = v1 - v3  # v1 - объект класса VectorInt

v1 = Vector(1, 2, 3, 4)
print(v1.get_coords())
v2 = Vector(2, 3, 4, 5)
print(v2.get_coords())
v = v1 - v2
print(v.get_coords())
print(type(v))
