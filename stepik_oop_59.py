"""
Подвиг 4. С помощью множественного наследования удобно описывать принадлежность объектов к нескольким разным группам.
Выполним такой пример.



Определите в программе классы в соответствии с их иерархией, представленной на рисунке выше:

Digit, Integer, Float, Positive, Negative

Каждый объект этих классов должен создаваться однотипной командой вида:

obj = Имя_класса(value)
где value - числовое значение. В каждом классе следует делать свою проверку на корректность значения value:

- в классе Digit: value - любое число;
- в классе Integer: value - целое число;
- в классе Float: value - вещественное число;
- в классе Positive: value - положительное число;
- в классе Negative: value - отрицательное число.

Если проверка не проходит, то генерируется исключение командой:

raise TypeError('значение не соответствует типу объекта')
После этого объявите следующие дочерние классы:

PrimeNumber - простые числа; наследуется от классов Integer и Positive;
FloatPositive - наследуется от классов Float и Positive.

Создайте три объекта класса PrimeNumber и пять объектов класса FloatPositive с произвольными допустимыми для них
значениями. Сохраните все эти объекты в виде списка digits.

Затем, используя функции isinstance() и filter(), сформируйте следующие списки из указанных объектов:

lst_positive - все объекты, относящиеся к классу Positive;
lst_float - все объекты, относящиеся к классу Float.
"""


class Digit():
    def __init__(self, value):
        super().__init__()
        if self.valid_value(value):
            self.value = value

    @staticmethod
    def valid_value(value):
        if type(value) in (int, float):
            return True
        else:
            raise TypeError('значение не соответствует типу объекта')


class Integer(Digit):
    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    def valid_value(value):
        if isinstance(value, int):
            return True
        else:
            raise TypeError('значение не соответствует типу объекта')


class Float(Digit):
    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    def valid_value(value):
        if isinstance(value, float):
            return True
        else:
            raise TypeError('значение не соответствует типу объекта')


class Positive(Digit):
    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    def valid_value(value):
        if type(value) in (int, float) and value > 0:
            return True
        else:
            raise TypeError('значение не соответствует типу объекта')


class Negative(Digit):
    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    def valid_value(value):
        if type(value) in (int, float) and value < 0:
            return True
        else:
            raise TypeError('значение не соответствует типу объекта')


class PrimeNumber(Integer, Positive):
    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    def valid_value(value):
        if isinstance(value, int) and Positive.valid_value(value):
            return True
        else:
            raise TypeError('значение не соответствует типу объекта')


class FloatPositive(Float, Positive):
    def __init__(self, value):
        super().__init__(value)

    @staticmethod
    def valid_value(value):
        if isinstance(value, float) and Positive.valid_value(value):
            return True
        else:
            raise TypeError('значение не соответствует типу объекта')



pr1 = PrimeNumber(1)
pr2 = PrimeNumber(2)
pr3 = PrimeNumber(3)

print(FloatPositive.__mro__)
fl1 = FloatPositive(0.1)
fl2 = FloatPositive(0.2)
fl3 = FloatPositive(0.3)
fl4 = FloatPositive(0.4)
fl5 = FloatPositive(0.5)

digits = [pr1, pr2, pr3, fl1, fl2, fl3, fl4, fl5]

lst_positive = list(filter(lambda item: isinstance(item, Positive), digits))
print(lst_positive)
lst_float = list(filter(lambda item: isinstance(item, Float), digits))
print(lst_float)