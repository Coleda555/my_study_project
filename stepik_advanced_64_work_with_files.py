'''
Подарок на новый год
Вам доступен текстовый файл class_scores.txt с оценками за итоговый тест на строках вида: фамилия оценка (фамилия и
оценка разделены пробелом). Оценка - целое число от 00 до 100100 включительно.

Напишите программу для добавления 55 баллов к каждому результату теста и вывода фамилий и новых результатов тестов в
файл new_scores.txt.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем new_scores.txt в соответствии с условием задачи.

Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.

Примечание 2. Если бы файл class_scores.txt содержал строки:
'''

with open('class_scores.txt', 'r', encoding='utf-8') as file_input:
    text = list(map(lambda line: line.split(), file_input.readlines()))
with open('new_scores.txt', 'w', encoding='utf-8') as file_output:
    text_output = list(map(lambda line: [line[0], int(line[1]) + 5], text))
    for line in text_output:
        # print(*line, file=file_output)
        if line[1] > 100:
            line[1] = 100
        file_output.write('{0} {1}\n'.format(line[0], line[1]))
