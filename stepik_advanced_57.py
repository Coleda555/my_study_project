"""
Опасный вирус 😈
В файловую систему компьютера, на котором развернута наша ❤️ платформа Stepik, проник опасный вирус и сломал контроль
 прав доступа к файлам. Говорят, вирус написал один из студентов курса Python для начинающих.

Для каждого файла известно, с какими действиями можно к нему обращаться:

запись W (write, доступ на запись в файл);
чтение R (read, доступ на чтение из файла);
запуск X (execute, запуск на исполнение файла).
Напишите программу для восстановления контроля прав доступа к файлам. Ваша программа для каждого запроса должна будет
возвращать OK если выполняется допустимая операция, и Access denied, если операция недопустима.

Формат входных данных
Программа получает на вход количество файлов nn, содержащихся в файловой системе компьютера. Далее идет nn строк, на
 каждой имя файла и допустимые с ним операции, разделенные символом пробела. В следующей строке записано число mm —
  количество запросов к файлам, и затем mm строк с запросами вида операция файл. Одному и тому же файлу может быть
  адресовано любое количество запросов.

Формат выходных данных
Программа должна вывести для каждого из mm запросов в отдельной строке Access denied или OK.

Тестовые данные 🟢
Sample Input 1:

5
my_pycode.exe W X
log_n X W R
ave R
lucky_m W R
dnsss.py W
6
execute ave
read dnsss.py
write log_n
execute log_n
read ave
write my_pycode.exe
Sample Output 1:

Access denied
Access denied
OK
OK
OK
OK
Sample Input 2:

2
marvel_movies X
dc_com X R
2
execute dc_com
write dc_com
Sample Output 2:

OK
Access denied
"""
dict_check = {'write': 'W', 'read': 'R', 'execute': 'X'}
n = int(input())
dict_files = {}
for _ in range(n):
    file_input = [item for item in input().split()]
    dict_files[file_input[0]] = file_input[1:]
print(dict_files)
m = int(input())
for _ in range(m):
    ask = [ask for ask in input().split()]
    if dict_check[ask[0]] in dict_files[ask[1]]:
        print('OK')
    else:
        print('Access denied')
