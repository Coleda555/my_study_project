"""
Функция filter_anagrams()
Анаграммы — это слова, которые состоят из одинаковых букв. Например:

адаптер — петарда
адресочек — середочка
азбука — базука
аистенок — осетинка
Реализуйте функцию filter_anagrams(), которая принимает два аргумента в следующем порядке:

word — слово в нижнем регистре
words — список слов в нижнем регистре
Функция должна возвращать список, элементами которого являются слова из списка words, которые представляют анаграмму
слова word. Если список words пуст или не содержит анаграмм, функция должна вернуть пустой список.

Примечание 1. Слова в возвращаемом функцией списке должны располагаться в своем исходном порядке.

Примечание 2. Считайте, что слово является анаграммой самого себя.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию filter_anagrams(), но не
код, вызывающий ее.
"""


def filter_anagrams(word, words):
    result = []
    for item in words:
        if len(word) == len(item):
            check = list(item)
            for ch in word:
                if ch in check:
                    check.remove(ch)
                else:
                    break
                if len(check) == 0:
                    result.append(item)
    return result


print(filter_anagrams('tommarvoloriddle', ['iamlordvoldemort', 'iamdevolremort', 'mortmortmortmort',
                                           'remortvolremort']))
