"""
Подвиг 10 (на повторение). Объявите класс EmailValidator для проверки корректности email-адреса. Необходимо запретить
создание объектов этого класса: при создании экземпляров должно возвращаться значение None, например:

em = EmailValidator() # None
В самом классе реализовать следующие методы класса (@classmethod):

check_email(cls, email) - возвращает True, если email записан верно и False - в противном случае;
get_random_email(cls) - для генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com, где x - любой
допустимый символ в email (латинский буквы, цифры, символ подчеркивания и точка).

Корректность строки email определяется по следующим критериям:

- допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
- длина email до символа @ не должна превышать 100 (сто включительно);
- длина email после символа @ не должна быть больше 50 (включительно);
- после символа @ обязательно должна идти хотя бы одна точка;
- не должно быть двух точек подряд.

Также в классе нужно реализовать приватный статический метод класса:

is_email_str(email) - для проверки типа переменной email, если строка, то возвращается значение True, иначе - False.

Метод is_email_str() следует использовать в методе check_email() перед проверкой корректности email. Если параметр
email не является строкой, то check_email() возвращает False.

Пример использования класса EmailValidator (эти строчки в программе писать не нужно):

res = EmailValidator.check_email("sc_lib@list.ru") # True
res = EmailValidator.check_email("sc_lib@list_ru") # False
P.S. В программе требуется объявить только класс. На экран ничего выводить не нужно.
"""
import string
import random


class EmailValidator:
    FOR_EMAIL = string.ascii_letters + string.digits + "._"

    def __new__(cls, *args, **kwargs):
        return None

    def __init__(self):
        pass

    @classmethod
    def check_email(cls, email: str):
        check_list = []
        if cls.__is_email_str(email):
            check_list.append(True)
        else:
            return False
        if email.count('@') == 1:
            check_list.append(True)
        else:
            return False
        email_list = email.split("@")
        if len(email_list[0]) <= 100 and len(email_list[1]) <= 50:
            check_list.append(True)
        else:
            return False
        if '.' in email_list[1] and email.count('..') == 0:
            check_list.append(True)
        else:
            return False
        if set(email_list[1]).issubset(set(cls.FOR_EMAIL)) and set(email_list[1]).issubset(set(cls.FOR_EMAIL)):
            check_list.append(True)
        else:
            return False
        return all(check_list)

    @classmethod
    def get_random_email(cls):
        domen = ['.ru', '.org', '.com', '.by', '.net', '.biz']
        get_email = ''
        for _ in range(1, random.randint(0, 100)):
            get_email += random.choice(cls.FOR_EMAIL)
        get_email += '@'
        for _ in range(0, random.randint(0, 46)):
            get_email += random.choice(cls.FOR_EMAIL)
        get_email += random.choice(domen)
        return get_email


    @staticmethod
    def __is_email_str(email):
        return isinstance(email, str)




