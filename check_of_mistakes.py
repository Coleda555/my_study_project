'''
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.

На вход программе первой строкой передаётся количество d известных нам слов, после чего на d строках указываются эти
слова. Затем передаётся количество l строк текста для проверки, после чего l строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

Sample Input:

4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic
Sample Output:

stepic
champignons
the
'''

d = int(input())
list_input = []
list_check = []
list_output = []

for i in range(d):
    list_input.append(input().lower())

l = int(input())

for i in range(l):
    list_check.extend([word for word in input().lower().split()])

print(list_input)
print(list_check)

for word in list_check:
    if word not in list_input:
        if word not in list_output:
            list_output.append(word)

print(*list_output, sep="\n")
