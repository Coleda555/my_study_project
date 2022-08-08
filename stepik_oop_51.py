"""
Подвиг 9 (на повторение). Объявите класс StringDigit, который наследуется от стандартного класса str. Объекты класса
StringDigit должны создаваться командой:

sd = StringDigit(string)
где string - строка из цифр (например, "12455752345950"). Если в строке string окажется хотя бы один не цифровой символ,
 то генерировать исключение командой:

raise ValueError("в строке должны быть только цифры")
Также в классе StringDigit нужно переопределить оператор + (конкатенации строк) так, чтобы операции:

sd = sd + "123"
sd = "123" + sd
создавали новые объекты класса StringDigit (а не класса str). Если же при соединении строк появляется не цифровой
символ, то генерировать исключение:

raise ValueError("в строке должны быть только цифры")
Пример использования класса (эти строчки в программе не писать):

sd = StringDigit("123")
print(sd)       # 123
sd = sd + "456" # StringDigit: 123456
sd = "789" + sd # StringDigit: 789123456
sd = sd + "12f" # ValueError
"""


class StringDigit(str):
    def __init__(self, string):
        self.string = ''
        if string.isdigit():
            self.string = string
        else:
            raise ValueError("в строке должны быть только цифры")

    def __str__(self):
        return self.string

    def __add__(self, other):
        result = None
        if isinstance(other, StringDigit):
            result = StringDigit(self.string + other.string)
        elif isinstance(other, str):
            if not other.isdigit():
                raise ValueError("в строке должны быть только цифры")
            else:
                result = StringDigit(self.string + other)
        return result

    def __radd__(self, other):
        if other.isdigit():
            return StringDigit(other + self.string)
        else:
            raise ValueError("в строке должны быть только цифры")



sd = StringDigit("123")
sd1 = StringDigit('345')
print('1', sd)  # 123
sd = sd + "456"  # StringDigit: 123456
print('2', sd)
sd = "789" + sd  # StringDigit: 789123456
print('3', sd)
#sd = sd + "12f" # ValueError
sd = sd + sd
print('4', sd)
