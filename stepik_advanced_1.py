"""
Standard American Convention
На вход программе подаётся натуральное число. Напишите программу, которая вставляет в заданное число запятые в
соответствии со стандартным американским соглашением о запятых в больших числах.

Формат входных данных
На вход программе подаётся натуральное число n,
Формат выходных данных
Программа должна вывести число с запятыми в соответствии с условием задачи.

Sample Input 1:

1000000
Sample Output 1:

1,000,000
Sample Input 2:

100
Sample Output 2:

100
Sample Input 3:

12345
Sample Output 3:

12,345
"""
num = input()


def amrecan_standart(number):
    first_num = ''
    if len(number) < 3:
        return number
    if len(number) % 3 > 0:
        first_num += number[0: len(number) % 3] + ','
    num_output = first_num
    counter = 0
    for i in str(number)[len(number) % 3:]:
        if counter // 3 > 0 and counter % 3 == 0:
            num_output += ','
        num_output += i
        counter += 1

    return num_output


print(amrecan_standart(num))
