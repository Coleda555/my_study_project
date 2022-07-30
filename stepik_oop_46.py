"""
Подвиг 7. С помощью наследования можно как бы "наполнять" дочерние классы нужными качествами (свойствами). Как пример,
объявите в программе класс с именем:

Singleton

который бы позволял создавать только один экземпляр (все последующие экземпляры должны ссылаться на первый). Как это
делать, вы должны уже знать из этого курса.

Затем, объявите еще один класс с именем:

Game

который бы наследовался от класса Singleton. Объекты класса Game должны создаваться командой:

game = Game(name)
где name - название игры (строка). В каждом объекте класса Game должен создаваться атрибут name с соответствующим
содержимым.

Убедитесь, что атрибут name принимает значение первого созданного объекта (если это не так, то поправьте инициализатор
дочернего класса, чтобы это условие выполнялось).
"""


class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if Singleton.__instance is None:
            Singleton.__instance = super().__new__(cls)
        return Singleton.__instance

    def __init__(self, name):
        self.name = name

class Game(Singleton):
    def __init__(self, name):
        if "name" not in self.__dict__:
            self.name = name

game1 = Game("CS")
game2 = Game("WOW")
game3 = Game("Tanks")

print(game1.name, game2.name, game3.name)