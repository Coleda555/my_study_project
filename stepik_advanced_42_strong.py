"""
Самое редкое слово 🌶️
На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего, без
 учета регистра. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести слово (в нижнем регистре), встречаемое реже всего.

Примечание 1. Программа не должна быть чувствительной к регистру, слова apple и Apple должна воспринимать как
одинаковые.

Примечание 2. Слово — последовательность букв. Кроме слов в тексте могут присутствовать пробелы и знаки препинания
.,!?:;-, которые нужно игнорировать. Других символов в тексте нет.

Тестовые данные 🟢
Номер теста	Входные данные	Выходные данные
1	home sweet home	sweet
2	home sweet home sweet.	home
3	How are you? how Are?	you
4	London is the capital of Great Britain. More than six million people live in London. London lies on both banks of
the river Thames. It is the largest city in Europe and one of the largest cities in the world. London is not only the
capital of the country, it is also a very big port, one of the greatest commercial centres in the world, a university
city, and the seat of the government of Great Britain!	also
5	My dear, here we must run as fast as we can, just to stay in place. And if you wish to go anywhere you must run
twice as fast as that.	and
6	I bought two books: a new book and an old book. The new book was more expensive than the old book.	a
7	наш курс курс самый самый лучший	лучший
Sample Input 1:

home sweet home
Sample Output 1:

sweet
Sample Input 2:

home sweet home sweet.
Sample Output 2:

home
"""
s = input().lower()
s_clean = ''
for ch in s:
    if ch not in '.,!?:;-':
        s_clean += ch
list_s = [word for word in s_clean.split()]
dict_words = {}
for word in list_s:
    if word not in dict_words:
        dict_words[word] = list_s.count(word)
mini = min(dict_words.values())
for key in sorted(dict_words):
    if dict_words[key] == mini:
        print(key)
        break
