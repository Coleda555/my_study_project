"""
Напишите программу, которая будет находить наилучшую покерную комбинацию в данной руке из 5 карт. Вальты, дамы, короли
 и тузы будут даны как числа 11, 12, 13 и 1 соответственно.

В любой карточной игре есть место шулерству, поэтому следует проверить руку на возможность ее существования. В руке из
пяти карт не может быть более 4 одинаковых карт, если такое произошло – следует вывести слово Шулер.

Комбинации по убыванию старшинства:

4 одинаковые карты – вывести Каре;
3 одинаковые карты и 2 другие одинаковые карты – вывести Фулл Хаус;
5 последовательно идущих карт – Стрит;
3 одинаковые карты – Сет;
2 одинаковые карты и 2 другие одинаковые карты – Две пары;
2 одинаковые карты – Пара;
ничего из вышеперечисленного – Старшая карта.
Формат входных данных
На вход программе подается 5 чисел от 1 до 13 через пробел – номера карт в руке.

Формат выходных данных
Вывести наилучшую возможную покерную комбинацию.

Примечание. Старший стрит (десятка, валет, дама, король, туз) не является стритом для упрощения задачи.

Sample Input 1:

4 6 5 7 8
Sample Output 1:

Стрит
Sample Input 2:

10 3 5 6 1
Sample Output 2:

Старшая карта
Sample Input 3:

5 5 5 5 5
Sample Output 3:

Шулер
Sample Input 4:

3 2 3 2 2
Sample Output 4:

Фулл Хаус
Sample Input 5:

10 10 10 10 4
Sample Output 5:

Каре """

input_cards = [int(i) for i in input().split()]

def poker(five_cards):
    amount_cards =[]
    for num in five_cards:
        amount = five_cards.count(num)
        if amount > 4:
            return 'Шулер'
        amount_cards.append(amount)

    if 4 in amount_cards:
        return 'Каре'
    elif 3 in amount_cards and 2 in amount_cards:
        return 'Фулл Хаус'
    elif 3 in amount_cards:
        return 'Сет'
    elif amount_cards.count(2) == 4:
        return 'Две пары'
    elif 2 in amount_cards:
        return 'Пара'

    five_cards.sort()
    counter = 0
    for i in range(len(five_cards) -1):
        if five_cards[i] == five_cards[i+1] - 1:
            counter +=1
    if counter == 4:
        return "Стрит"
    return "Старшая карта"

print(poker(input_cards))
