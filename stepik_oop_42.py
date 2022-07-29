"""
Подвиг 4. Известно, что в Python мы можем соединять два списка между собой с помощью оператора +:

lst = [1, 2, 3] + [4.5, -3.6, 0.78]
Но нет реализации оператора -, который бы убирал из списка все значения вычитаемого списка:

lst = [1, 2, 3, 4, 5, 6] - [5, 6, 7, 8, 1] # [2, 3, 4] (порядок следования оставшихся элементов списка должен
сохраняться)
Давайте это поправим и создадим такой функционал. Для этого нужно объявить класс с именем NewList, объекты которого
создаются командами:

lst = NewList() # пустой список
lst = NewList([-1, 0, 7.56, True]) # список с начальными значениями
Реализуйте для этого класса работу с оператором вычитания, чтобы над объектами класса NewList можно было выполнять
следующие действия:

lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
Также в классе NewList необходимо объявить метод:

get_list() - для возвращения результирующего списка объекта класса NewList

Например:

lst = res_2.get_list() # [1, 2, 3]
"""


class NewList:
    def __init__(self, args=None):
        self.lst = []
        if args != None:
            self.lst = [] + args
        print('проверка объекта класса', self.lst)

    def get_list(self):
        return self.lst

    @staticmethod
    def __subtraction(lst1, lst2):
        lst1_copy = lst1.copy()
        lst2_copy = lst2.copy()
        print(lst1, lst2)
        print(lst1_copy, lst2_copy)

        for i in range(len(lst1)):
            for j in range(len(lst2)):
                # print('check', lst1_copy[i], lst2_copy[j], type(lst1_copy[i]), type(lst2_copy[j]))
                if lst1_copy[i] == lst2_copy[j] and type(lst1_copy[i]) is type(lst2_copy[j]):
                    # print('+++', lst1_copy[i], lst2_copy[j])
                    lst1_copy[i] = '*'
                    lst2_copy[j] = '*'
                else:
                    pass
                    # print('---', lst1_copy[i], lst2_copy[j])

        return [item for item in lst1_copy if item != '*']

    def __sub__(self, other):
        other_lst = None
        if isinstance(other, list):
            other_lst = other
        elif isinstance(other, NewList):
            other_lst = other.get_list()

        return NewList(self.__subtraction(self.lst, other_lst))

    def __rsub__(self, other):
        other_lst = []
        if isinstance(other, list):
            other_lst = other
        elif isinstance(other, NewList):
            other_lst = other.get_list()

        return NewList(self.__subtraction(other_lst, self.lst))


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
lst5 = NewList()
res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
print("res_1 [-4, 6, 10, 11, 15, False] *****   ", res_1.get_list())
lst1 -= lst2  # NewList: [-4, 6, 10, 11, 15, False]
print("lst1 [-4, 6, 10, 11, 15, False] *****   ", lst1.get_list())
res_2 = lst2 - [0, True]  # NewList: [1, 2, 3]
print("res_2  [1, 2, 3] ****   ", res_2.get_list())
res_3 = [1, 2, 3, 4.5] - res_2  # NewList: [4.5]
print("res_3", res_3.get_list())
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
print("res_4 [1, 2] *****    ", res_4.get_list())
print()
