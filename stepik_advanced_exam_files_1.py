'''Forbidden words 🌶️
На вход программе подается строка текста с именем текстового файла. Напишите программу, выводящую на экран содержимое
 этого файла, но с заменой всех запрещенных слов звездочками * (количество звездочек равно количеству букв в слове).

Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле forbidden_words.txt. Гарантируется, что все
слова в этом файле записаны в нижнем регистре.

Формат входных данных
На вход программе подается строка текста с именем существующего текстового файла, в котором необходимо заменить
запрещенные слова звездочками.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание 1. Ваша программа должна заменить запрещенные слова, где бы они ни встречались, даже если они встречаются в
середине другого слова.

Примечание 2. Программа должна заменять запрещенные слова независимо от их регистра. Например, если файл
forbidden_words.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и подобные должны быть заменены
на ****.

Примечание 3. Если бы файл forbidden_words.txt содержал слова:

hello email python the exam wor is
а файл в котором заменяются слова имел бы вид:

Hello, world! Python IS the programming language of thE future. My EMAIL is....
PYTHON is awesome!!!!
то результатом будет:

*****, ***ld! ****** ** *** programming language of *** future. My ***** **....
****** ** awesome!!!!
Примечание 4. Файл forbidden_words.txt можно скачать по ссылке. Ваша программа прогоняется на трех файлах data.txt,
stepik.txt и beegeek.txt.'''

name = input()
with open(name, 'r', encoding='utf-8') as file_input:
    text_input = file_input.read()

with open('forbidden_words.txt', 'r', encoding='utf-8') as file_ban:
    ban_words = [word.strip() for word in file_ban.read().split()]

ban_dict = {}
for word in ban_words:
    if word in text_input.lower():
        ban_dict[word] = text_input.lower().count(word)

for key in ban_dict:
    for _ in range(ban_dict[key]):
        index = text_input.lower().index(key)
        text_input = text_input[:index] + '*' * len(key) + text_input[index + len(key):]

print(text_input)
