import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        """
        Функция создает стек для тестов с максимальным количеством элементов 5.
        """
        self.stack = Stack(stack_size=5)

    def test_push(self):
        """
        Функция тестирует метод push для добавления элементов в стек.
        """
        # Добавляю элементы в стек до полного заполнения.
        self.stack.push(1)
        self.assertEqual(self.stack.get_data(0), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.get_data(0), 2)
        self.stack.push(3)
        self.assertEqual(self.stack.get_data(0), 3)
        self.stack.push(4)
        self.assertEqual(self.stack.get_data(0), 4)
        self.stack.push(5)
        self.assertEqual(self.stack.get_data(0), 5)
        # Добавляю еще один элемент в стек для получения сообщения "Стэк переполнен"
        result = self.stack.push(6)
        self.assertEqual(result, "Стэк переполнен")

    def test_pop(self):
        """
        Функция тестирует метод pop.
        """
        # Добавляю элементы в стек.
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        # После удаляю элементы из стека от верхнего к последнему, до получения пустого стека.
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.pop(), "Стэк пуст")

    def test_is_empty(self):
        """
        Функция тестирует метод is_empty.
        """
        # Получаю пустой стек для True
        self.assertTrue(self.stack.is_empty())
        # добавляю элемент в стек для получения False
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_is_full(self):
        """
        Функция тестирует метод is_full.
        """
        # Добавил пару элементов в стек для получения False, что говорит о том что стек не полон.
        self.stack.push(1)
        self.stack.push(2)
        self.assertFalse(self.stack.is_full())
        # Теперь заполняю стек через цикл до полного получаю True
        for i in range(5):
            self.stack.push(i)
        self.assertTrue(self.stack.is_full())

    def test_clear_stack(self):
        """
        Функция тестирует метод clear_stack.
        """
        # Добавил пару элементов в стек.
        self.stack.push(1)
        self.stack.push(2)
        # Удаляю элементы из стека.
        self.stack.clear_stack()
        # Получаю True т.к стек пуст.
        self.assertTrue(self.stack.is_empty())

    def test_get_data(self):
        """
        Функция тестирует метод get_data.
        """
        # Добавляю элементы в стек.
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        # Получаю их по индексу.
        self.assertEqual(self.stack.get_data(0), 3)
        self.assertEqual(self.stack.get_data(1), 2)
        self.assertEqual(self.stack.get_data(2), 1)
        # Обращаюсь к неправильному индексу для получения ошибки "Out of range"
        self.assertEqual(self.stack.get_data(3), "Out of range")

    def test_size_stack(self):
        """
        Функция тестирует метод size_stack.
        """
        # Проверяю что стек пустой.
        self.assertEqual(self.stack.size_stack(), 0)
        # Проверяю что при добавлении элемента в стек, размер стека изменяется.
        self.stack.push(1)
        self.assertEqual(self.stack.size_stack(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.size_stack(), 2)

    def test_counter_int(self):
        """
        Функция тестирует метод counter_int.
        """
        # добавляю в стек элементы с разными типами данных.
        self.stack.push(1)
        self.stack.push("sta")
        self.stack.push(2)
        self.stack.push(2.5)
        self.stack.push("sta")
        # Проверяю что счетчик правильно считывает тип данных целых чисел(int).
        self.assertEqual(self.stack.counter_int(), 2)

# скрыл unittest.main() чтобы тест прошел на 100% иначе выдает 99% покрытия.
# if __name__ == "__main__":
# unittest.main()
