"""
Тайный друг 🌶️
Напишите программу, которая случайным образом назначает каждому ученику его тайного друга, который будет вместе с ним
решать задачи по программированию.

Формат входных данных
На вход программе в первой строке подается число nn – общее количество учеников. Далее идут nn строк, содержащих имена
и фамилии учеников.

Формат выходных данных
Программа должна вывести имя и фамилию ученика (в соответствии с исходным порядком) и имя и фамилию его тайного друга,
 разделённые дефисом.

Примечание 1. Обратите внимание, что нельзя быть тайным другом самому себе и нельзя быть тайным другом для нескольких
учеников.

Примечание 2. Приведенные ниже тесты это лишь образцы возможного ответа. Возможны и другие способы выбора тайных друзей.

Для отладки кода 🟡
Тестовые данные 🟢
Sample Input 1:

3
Светлана Зуева
Аркадий Белых
Борис Боков
Sample Output 1:

Светлана Зуева - Борис Боков
Аркадий Белых - Светлана Зуева
Борис Боков - Аркадий Белых
Sample Input 2:

5
Владимир Смолов
Тагир Хан
Давид Лавров
Арина Приходько
Глеб Анисимов
Sample Output 2:

Владимир Смолов - Тагир Хан
Тагир Хан - Арина Приходько
Давид Лавров - Глеб Анисимов
Арина Приходько - Владимир Смолов
Глеб Анисимов - Давид Лавров
Sample Input 3:

2
Руслан Адашев
Святослав Герасимов
Sample Output 3:

Руслан Адашев - Святослав Герасимов
Святослав Герасимов - Руслан Адашев
"""
import random

n = int(input())
names = []
for _ in range(n):
    names.append(input())
shuffle_names = names.copy()
random.shuffle(shuffle_names)


def secret_friend(n: int, names: list, shuffle_names: list):
    if len(names) == 2:
        print('{0} - {1}'.format(names[0], names[1]))
        print('{0} - {1}'.format(names[1], names[0]))
        return
    names_output = {}
    names_check = {}
    for name in names:
        for i in range(len(shuffle_names)):
            if name != shuffle_names[i] and names_check.get(name) != shuffle_names[i]:
                names_output[name] = shuffle_names[i]
                names_check[shuffle_names[i]] = name
                del shuffle_names[i]
                break
    if len(names_output) == n:
        for key, value in names_output.items():
            print('{0} - {1}'.format(key, value))

    else:
        shuffle_names.clear()
        shuffle_names = names.copy()
        random.shuffle(shuffle_names)
        secret_friend(n, names, shuffle_names)


secret_friend(n, names, shuffle_names)

