"""
Функция spell()
Реализуйте функцию spell(), которая принимает произвольное количество позиционных аргументов-слов и возвращает словарь,
ключи которого — первые буквы слов, а значения — максимальные длины слов на эту букву.

Примечание 1. Если в функцию не передается ни одного аргумента, функция должна возвращать пустой словарь.

Примечание 2. Функция должна игнорировать регистр слов, при этом в результирующий словарь должны попасть именно буквы в
нижнем регистре.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию, но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылке.

Sample Input 1:

words = ['россия', 'Австрия', 'австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']

print(spell(*words))
Sample Output 1:

{'р': 7, 'а': 9, 'у': 10, 'к': 5}
Sample Input 2:

print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))
Sample Output 2:

{'м': 10, 'и': 11, 'х': 5, 'б': 8}
Sample Input 3:

words = ['fruit', 'football', 'February', 'forest', 'Family']
print(spell(*words))
Sample Output 3:

{'f': 8}
"""


def spell(*words):
    result = {}
    for word in words:
        if word.lower()[0] not in result:
            length_word = 0
            for value in words:
                if value.lower()[0] == word.lower()[0] and len(value) > length_word:
                    length_word = len(value)
            result[word.lower()[0]] = length_word
    return result


words = ['россия', 'Австрия', 'австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']

print(spell(*words))

