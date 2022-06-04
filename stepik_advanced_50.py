"""
Секретное слово
Напишите программу для расшифровки секретного слова методом частотного анализа.

Формат входных данных
В первой строке задано зашифрованное слово. Во второй строке задано одно целое число nn – количество букв в словаре. В
следующих nn строках записано, сколько раз конкретная буква алфавита встречается в этом слове – <буква>: <частота>.

Формат выходных данных
Программа должна вывести дешифрованное слово.

Примечание. Гарантируется, что частоты букв не повторяются.

Тестовые данные 🟢
Sample Input 1:

*!*!*?
3
а: 3
н: 2
с: 1
Sample Output 1:

ананас
Sample Input 2:

pop
2
д: 2
е: 1
Sample Output 2:

дед
"""
encryption = input()
encryption_dig = ''
for ch in encryption:
    encryption_dig += str(encryption.count(ch))
n = int(input())
dict_encryption = {}
for _ in range(n):
    s = input()
    dict_encryption[s[-1]] = s[0]
dechiper = ''
for num in encryption_dig:
    dechiper += dict_encryption[num]
print(dechiper)
