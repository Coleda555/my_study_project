"""
Слияние словарей 🌶️
Напишите функцию merge(), объединяющую словари в один общий. Функция должна принимать список словарей и возвращать
словарь, каждый ключ которого содержит множество (тип данных set) уникальных значений собранных из всех словарей
переданного списка.

Примечание 1. Следующий программный код:

result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
создает словарь:

result = {'a': {1, 5}, 'b': {2, 10, 17}, 'c': {50, 100}, 'd': {777}}
Примечание 2. Вызывать функцию merge() не нужно, требуется только реализовать.

Примечание 3. Слияние пустых словарей должно быть пустым словарем.

Для отладки кода 🟡
"""

def merge(values):
    set_keys = set()
    for item in values:
        for key in item:
            set_keys.add(key)
    result_output = {}
    for key in set_keys:
        result_output[key] = set()
    for key in set_keys:
        for item in values:
            if key in item:
                result_output[key].add(item[key])
    return result_output


result = ([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
print(merge(result))
print(merge([]))