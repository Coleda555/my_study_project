"""
Scrabble game
В игре Scrabble каждая буква приносит определенное количество баллов. Общая стоимость слова – сумма баллов его букв.
Чем реже буква встречается, тем больше она ценится:

Баллы	Буква
1	AA, EE, II, LL, NN, OO, RR, SS, TT, UU
2	DD, GG
3	BB, CC, MM, PP
4	FF, HH, VV, WW, YY
5	KK
8	JJ, XX
10	QQ, ZZ
Напишите программу подсчета итоговой стоимости введенного слова.

Формат входных данных
На вход программе подается одно слово в верхнем регистре на английском языке.

Формат выходных данных
Программа должна вывести суммарную стоимость букв введеного слова.

Примечание. Подробнее про игру можно почитать тут.

Тестовые данные 🟢
Sample Input 1:

DANSER
Sample Output 1:

7
Sample Input 2:

FRESHENER
Sample Output 2:

15
Sample Input 3:

ZIP
Sample Output 3:

14
"""
dict_values = {1: ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'], 2: ['D', 'G'], 3: ['B', 'C', 'M', 'P'], 4: [
    'F', 'H', 'V', 'W', 'Y'], 5: ['K'], 8: ['J', 'X'], 10: ['Q', 'Z']}
str_input = input()
total = 0
for ch in str_input:
    for key, value in dict_values.items():
        if ch in value:
            total += key
print(total)
