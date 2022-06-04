"""
Анаграммы 2
На вход программе подаются два предложения. Напишите программу, которая определяет, являются они анаграммами или нет.
 Ваша программа должна игнорировать регистр символов, знаки препинания и пробелы.

Формат входных данных
На вход программе подаются два предложения, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести YES , если предложения – анаграммы и NO в противном случае.

Примечание. Кроме слов в тексте могут присутствовать пробелы и знаки препинания .,!?:;-. Других символов в тексте нет.

Тестовые данные 🟢
Sample Input 1:

Вижу зверей
Живу резвей
Sample Output 1:

YES
Sample Input 2:

Когда увидимся
тогда и свидимся
Sample Output 2:

NO
Sample Input 3:

С мая весной
сам я не свой
Sample Output 3:

YES
"""
list_input = [input().lower() for i in range(2)]
s1 = ''
s2 = ''
for ch in list_input[0]:
    if ch not in '.,!?:;- ':
        s1 += ch
for ch in list_input[1]:
    if ch not in '.,!?:;- ':
        s2 += ch
dict1 = {}
for ch in s1:
    if ch not in dict1:
        dict1[ch] = s1.count(ch)
dict2 = {}
for ch in s2:
    if ch not in dict2:
        dict2[ch] = s2.count(ch)
if dict1 == dict2:
    print("YES")
else:
    print("NO")