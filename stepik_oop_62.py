"""
Подвиг 4. В программе вводятся два значения в одну строчку через пробел. Значениями могут быть числа, слова, булевы
величины (True/False). Необходимо прочитать эти значения из входного потока. Если оба значения являются числами, то
вычислить их сумму, иначе соединить их в одну строку с помощью оператора + (конкатенации строк). Результат вывести на
экран (в блоке finally).
"""

lst_in = input().split()


def check(lst_in):
    result = []
    result_str = ''
    for value in lst_in:
        try:
            value = int(value)
            result.append(value)
        except:
            try:
                value = float(value)
                result.append(value)
            except:
                result.append(value)

    if all(map(lambda x: type(x) in (float, int), result)):
        return sum(result)
    else:
        for elem in result:
            if type(elem) != str:
                result_str += str(elem)
            else:
                result_str += elem
        return result_str


print(check(lst_in))
