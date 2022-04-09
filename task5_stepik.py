"""
Назовем строку текста «почти палиндромом», если найдется такой буквенный символ, при удалении которого строка станет палиндромом.
При этом все символы, кроме букв, должны игнорироваться.

Напишите программу, которая определяет, является ли строка «почти палиндромом».

Формат входных данных
На вход программе подается строка текста, состоящая только из букв латинского алфавита в нижнем регистре,
цифр и символов !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~. Длина строки не превышает 300000300000 символов. Гарантируется, что строка содержит как минимум две буквы.

Формат выходных данных
Программа должна вывести True, если введенная строка является «почти палиндромом», или False в противном случае.

Примечание. Палиндром читается одинаково в обоих направлениях, например слово «rotavator».

Sample Input 1:

1kilg%rli8k
Sample Output 1:

True
Sample Input 2:

kkkkkkkkkee
Sample Output 2:

False
Sample Input 3:

#14&*@(a)!(@14112)!@$)!@*$!*a)$*099
Sample Output 3:

True
Sample Input 4:

ekkkkkkkkkkkkkkkkkkkkkk
Sample Output 4:

True
"""


def find_palindrom(palindrom):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    almost_palindrom = ''
    index = -1
    for char in palindrom:
        if char in alphabet:
            almost_palindrom += char
    for i in range(0, len(almost_palindrom) // 2):
        if almost_palindrom[i] != almost_palindrom[index]:
            if almost_palindrom[i] == almost_palindrom[index - 1]:
                if index == -1:
                    almost_palindrom = almost_palindrom[:index]
                else:
                    almost_palindrom = almost_palindrom[:index] + almost_palindrom[index + 1:]
            else:
                almost_palindrom = almost_palindrom[:i] + almost_palindrom[i + 1:]
        index -= 1
    return almost_palindrom == almost_palindrom[::-1]


print(find_palindrom('1kilg%rli8k'))  # True
print(find_palindrom('kkkkkkkkkee'))  # False
print(find_palindrom('#14&*@(a)!(@14112)!@$)!@*$!*a)$*099'))  # True
