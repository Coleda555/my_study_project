"""
Реализуйте класс PiggyBank, который представляет собой олдскульную копилку в форме свиньи. Он имеет два атрибута,
доллары (dollars) и центы (cents), и их начальные значения передаются в конструктор.

Создайте метод add_money с двумя параметрами deposit_dollars и deposit_cents, который увеличивает сумму денег в копилке.
 Например, если вы положили в копилку меньше доллара, значение deposit_dollars равно 0. Метод не должен ничего печатать!

Параметры deposit_dollars и deposit_cents метода add_money могут иметь любое значение, но значение центов в копилке
после добавления не может превышать 99! Если значение deposit_cents после добавления больше 99, вам необходимо обновить
 как значение в долларах, так и значение в центах!

Подсказка: вы можете использовать оператор целочисленного деления и деления с остатком!
"""


class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        self.cents += deposit_cents
        if self.cents > 99:
            self.dollars += self.cents // 100
            self.cents = self.cents % 100

#check
pepa = PiggyBank(5, 10)
pepa.add_money(5, 20)
pepa.add_money(5, 100)
print("Your deposit is {0} dollars and {1} cents".format(pepa.dollars, pepa.cents)) #Your deposit is 16 dollars and 30 cents