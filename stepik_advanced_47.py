"""
Словарь синонимов
Вам дан словарь, состоящий из пар слов-синонимов. Повторяющихся слов в словаре нет. Напишите программу, которая для
 одного данного слова определяет его синоним.

Формат входных данных
На вход программе подается количество пар синонимов nn. Далее следует nn строк, каждая строка содержит два
слова-синонима. После этого следует одно слово, синоним которого надо найти.

Формат выходных данных
Программа должна вывести одно слово, синоним введенного.

Примечание 1. Гарантируется, что синоним введенного слова существует в словаре.

Примечание 2. Все слова в словаре начинаются с заглавной буквы.

Тестовые данные 🟢
Sample Input 1:

4
Awful Terrible
Beautiful Pretty
Great Excellent
Generous Bountiful
Pretty
Sample Output 1:

Beautiful
Sample Input 2:

3
Kind Affable
Intellect Mind
Popular Celebrated
Popular
Sample Output 2:

Celebrated
"""
n = int(input())
dict_input = {}
list_input = []
for _ in range(n):
    list_input = [word for word in input().split()]
    dict_input[list_input[0]] = list_input[1]
word = input()
for key, value in dict_input.items():
    if key == word:
        print(value)
    elif value == word:
        print(key)
