"""
Анаграммы 1
Анаграмма – слово (словосочетание), образованное путём перестановки букв, составляющих другое слово (или словосочетание)
. Например, английские слова evil и live – это анаграммы.

На вход программе подаются два слова. Напишите программу, которая определяет, являются ли они анаграммами.

Формат входных данных
На вход программе подаются два слова, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести YES если слова являются анаграммами и NO в противном случае.

Тестовые данные 🟢
Sample Input 1:

thing
night
Sample Output 1:

YES
Sample Input 2:

cat
rat
Sample Output 2:

NO
Sample Input 3:

tea
eat
Sample Output 3:

YES
"""

list_input = [input().lower() for i in range(2)]
dict1 = {}
for ch in list_input[0]:
    if ch not in dict1:
        dict1[ch] = list_input[0].count(ch)
dict2 = {}
for ch in list_input[1]:
    if ch not in dict2:
        dict2[ch] = list_input[1].count(ch)
if dict1 == dict2:
    print("YES")
else:
    print("NO")
