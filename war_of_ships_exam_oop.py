import random as rd


class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self._length = length
        self._tp = tp  # ориентация корабля (1 - горизонтальная; 2 - вертикальная).
        self._x = x
        self._y = y
        self._is_move = True
        self._cells = [1 for _ in range(self._length)]

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y

    def get_start_coords(self):
        return self._x, self._y

    def move(self, go):
        if self._is_move:
            if self._tp == 1:
                self._x += go
            elif self._tp == 2:
                self._y += go

    # проверка на столкновение с другим кораблем ship (столкновением считается, если другой корабль или пересекается с
    # текущим или просто соприкасается, в том числе и по диагонали); метод возвращает True, если столкновение есть и
    # False - в противном случае
    def is_collide(self, ship):
        ship_1_coords = []
        ship_2_coords = []
        if ship._tp == 1:
            for y in range(ship._y - 1, ship._y + 2):
                for x in range(ship._x - 1, ship._x + ship._length + 1):
                    if y < 0:
                        y = 0
                    elif x < 0:
                        x = 0
                    ship_1_coords.append((y, x))
        elif ship._tp == 2:
            for y in range(ship._y - 1, ship._y + ship._length + 1):
                for x in range(ship._x - 1, ship._x + 2):
                    if y < 0:
                        y = 0
                    elif x < 0:
                        x = 0
                    ship_1_coords.append((y, x))
        if self._tp == 1:
            for i in range(self._x, self._x + self._length):
                ship_2_coords.append((self._y, i))
        elif self._tp == 2:
            for i in range(self._y, self._y + self._length):
                ship_2_coords.append((i, self._x))
        for item in ship_2_coords:
            if item in ship_1_coords:
                return True
        return False




    # проверка на выход корабля за пределы игрового поля (size - размер игрового поля, обычно, size = 10); возвращается
    # булево значение True, если корабль вышел из игрового поля и False - в противном случае
    def is_out_pole(self, size):
        if self._tp == 1:
            if self._x + self._length > size:
                return True
        if self._tp == 2:
            if self._y + self._length > size:
                return True
        return False

    def __getitem__(self, item):
        if 0 <= item < len(self._cells):
            return self._cells[item]

    def __setitem__(self, key, value):
        if 0 <= key < len(self._cells):
            self._cells[key] = value


class GamePole:
    def __init__(self, size):
        self._size = size
        self._ships = []
        self._pole = [[0] * self._size for _ in range(self._size)]

    # начальная инициализация игрового поля; здесь создается список из кораблей (объектов класса Ship): однопалубных - 4;
    # двухпалубных - 3; трехпалубных - 2; четырехпалубный - 1 (ориентация этих кораблей должна быть случайной).
    def init(self):
        self._ships = [Ship(4, tp=rd.randint(1, 2)), Ship(3, tp=rd.randint(1, 2)), Ship(3, tp=rd.randint(1, 2)),
                       Ship(2, tp=rd.randint(1, 2)), Ship(2, tp=rd.randint(1, 2)), Ship(2, tp=rd.randint(1, 2)),
                       Ship(1, tp=rd.randint(1, 2)), Ship(1, tp=rd.randint(1, 2)), Ship(1, tp=rd.randint(1, 2)),
                       Ship(1, tp=rd.randint(1, 2))]

        for ship in self._ships:
            flag = True
            while flag:
                ship.set_start_coords(rd.randint(0, 9 - ship._length), rd.randint(0, 9 - ship._length))
                if self.check_place(ship):
                    if ship._tp == 1:
                        for i in range(ship._length):
                            self._pole[ship._y][ship._x + i] = ship[i]

                    elif ship._tp == 2:
                        for i in range(ship._length):
                            self._pole[ship._y + i][ship._x] = ship[i]

                    flag = False



    def get_ships(self):
        return self._ships

    def move_ships(self):
        for ship in self._ships:
            pass


    def show(self):
        for cells in self.get_pole():
            print(*cells)

    def get_pole(self):
        ls_tp = []
        for line in self._pole:
            ls_tp.append(tuple(line))
        return tuple(ls_tp)


    def check_place(self, ship):
        if ship._tp == 1:
            try:
                for y in range(ship._y - 1, ship._y + 2):
                    for x in range(ship._x - 1, ship._x + ship._length + 1):
                        if y < 0:
                            y = 0
                        elif x < 0:
                            x = 0
                        if self._pole[y][x] == 1:
                            return False
                return True
            except IndexError:
                pass

        elif ship._tp == 2:
            try:
                for y in range(ship._y - 1, ship._y + ship._length + 1):
                    for x in range(ship._x - 1, ship._x + 2):
                        if y < 0:
                            y = 0
                        elif x < 0:
                            x = 0
                        if self._pole[y][x] == 1:
                            return False
                return True
            except IndexError:
                pass


SIZE_GAME_POLE = 10

pole = GamePole(SIZE_GAME_POLE)
pole.init()
print(pole.get_pole())
