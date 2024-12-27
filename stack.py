class Node:
    """
    Class Node - узел в связанном списке.
    Атрибуты:
        data: Данные, которые хранятся в узле.
        next_node: следующий узел в списке
    """

    def __init__(self, data, next_node=None):
        """
        Функция инициализирует узел с данными и ссылкой на следующий узел.

        :param data: Данные, которые хранятся в узле.
        :param next_node: Следующий узел в списке. По умолчанию None
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """
    Class Stack реализует стек с заданным размером.

    Атрибуты:
        stack_size: Максимальный размер стека
        top: Ссылка на верхний элемент стека
    """

    def __init__(self, stack_size=5, top=None):
        """
        Функция инициализирует стек с заданным размером и вершиной.

        :param stack_size: Максимальный размер стека. По умолчанию 5.
        :param top: Верхний элемент. По умолчанию None.
        """
        self.stack_size = stack_size
        self.top = top  # через топ обращаемся к атрибутам ноды

    def push(self, data):
        """
        Функция добавляет новый элемент в стек

        :param data: Данные для добавления в стек
        :return: Возвращает сообщение о переполнении стека, при условии если он полон.
        """
        if self.size_stack() < self.stack_size:
            new_node = Node(data)
            new_node.next_node = self.top  # та вершина которая была
            self.top = new_node  # переназначаем вершину
        else:
            # print("Стэк переполнен")
            return "Стэк переполнен"

    def pop(self):
        """
        Функция удаляет и возвращает верхний элемент стека

        :return: Возвращает данные удаленного стека, либо выводит сообщение если стек пуст.
        """
        if self.top:
            remove_last = self.top
            self.top = self.top.next_node
            return remove_last.data
        else:
            return "Стэк пуст"

    def is_empty(self):
        """
        Функция проверяет, пустой ли стек.

        :return: Возвращает True, если стек пуст. Иначе False если нет.
        """
        if self.top:
            return False
        else:
            return True

    def is_full(self):
        """
        Функция проверяет полон ли стек.

        :return: Возвращает True, если он полон. Иначе False если нет.
        """
        if self.stack_size == self.size_stack():
            return True
        else:
            return False

    def clear_stack(self):
        """
        Функция удаляет все элементы стека
        """
        while self.top:
            self.pop()

    def get_data(self, index):
        """
        Функция возвращает данные элемента стека по индексу

        :param index: Индекс элемента
        :return: Возвращает данные элемента или выводит сообщение об ошибке, если индекс не входит в диапазон.
        """
        counter = 0
        stack_item = self.top
        while stack_item:
            if counter == index:
                return stack_item.data
            stack_item = stack_item.next_node
            counter += 1
        return f"Out of range"

    def size_stack(self):
        """
        Функция возвращает количество элементов в стеке

        :return: Возвращает число элементов в стеке
        """
        counter = 0
        stack_item = self.top
        while stack_item:
            counter += 1
            stack_item = stack_item.next_node
        return counter

    def counter_int(self):
        """
        Функция счетчик целых чисел в стеке.

        :return: Возвращает количество целых чисел в стеке
        """
        counter = 0
        stack_item = self.top
        while stack_item:
            if isinstance(stack_item.data, int):
                counter += 1
            stack_item = stack_item.next_node
        return counter


stack = Stack()
stack.push(1)
stack.push("sta")
stack.push(2)
stack.push(2.5)
stack.push("sta")
# Убрал print() чтобы в тесте не мешали, а то напрягали когда постоянно выводятся.
# print(stack.counter_int())

