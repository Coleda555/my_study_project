"""
Подвиг 5. Объявите класс LinkedList (связный список) для работы со следующей структурой данных:



Здесь создается список из связанных между собой объектов класса ObjList. Объекты этого класса создаются командой:

obj = ObjList(data)
где data - строка с некоторой информацией. Также в каждом объекте obj класса ObjList должны создаваться следующие
локальные атрибуты:

__data - ссылка на строку с данными;
__prev - ссылка на предыдущий объект связного списка (если объекта нет, то __prev = None);
__next - ссылка на следующий объект связного списка (если объекта нет, то __next = None).

В свою очередь, объекты класса LinkedList должны создаваться командой:

linked_lst = LinkedList()
и содержать локальные атрибуты:

head - ссылка на первый объект связного списка (если список пуст, то head = None);
tail - ссылка на последний объект связного списка (если список пуст, то tail = None).

А сам класс содержать следующие методы:

add_obj(obj) - добавление нового объекта obj класса ObjList в конец связного списка;
remove_obj(indx) - удаление объекта класса ObjList из связного списка по его порядковому номеру (индексу); индекс
отсчитывается с нуля.

Также с объектами класса LinkedList должны поддерживаться следующие операции:

len(linked_lst) - возвращает число объектов в связном списке;
linked_lst(indx) - возвращает строку __data, хранящуюся в объекте класса ObjList, расположенного под индексом indx (в
связном списке).
"""


class ObjList:
    def __init__(self,  data):
        self.__data = ''
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is str:
            self.__data = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        if type(value) in (ObjList, type(None)):
            self.__prev = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        if type(value) in (ObjList, type(None)):
            self.__next = value

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        obj.prev = self.tail

        if self.tail:
            self.tail.next = obj
        self.tail = obj

        if not self.head:
            self.head = obj

    def __get_obj_by_index(self, indx):
        h = self.head
        n = 0
        while n and n < indx:
            h = h.next
            n += 1
        return h

    def remove_obj(self, indx):
        obj = self.__get_obj_by_index(indx)
        if obj is None:
            return

        p, n = obj.prev, obj.next
        if p:
            p.next = n
        if n:
            n.prev = p

        if self.head == obj:
            self.head = n
        if self.tail == obj:
            self.tail = p

    def __len__(self):
        n = 0
        h = self.head
        while h:
            n += 1
            h = h.next
        return n

    def __call__(self, indx, *args, **kwargs):
        obj = self.__get_obj_by_index(indx)
        return obj.data if obj else None



