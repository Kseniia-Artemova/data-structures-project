class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data: dict) -> None:
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        :param next_node: ссылка на следующий в списке объект класса
        """

        self.data = data
        self.__next_node = None

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node) -> None:
        self.__next_node = next_node

    def __str__(self) -> str:
        """Возвращает строку data класса в формате строки"""

        return f"{self.data}"


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self) -> None:
        """
        Конструктор класса LinkedList

        :param head: ссылка на первый объект списка
        :param tail: ссылка на последний объект списка
        """

        self.__head = None
        self.__tail = None

    @property
    def head(self) -> Node:
        return self.__head

    @property
    def tail(self) -> Node:
        return self.__tail

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""

        new_node = Node(data)

        if self.head:
            current_head = self.head

            if self.head.next_node is None:
                self.__tail = current_head
            self.__head = new_node
            new_node.next_node = current_head

        else:
            self.__head = self.__tail = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""

        new_node = Node(data)

        if self.tail:
            current_tail = self.tail
            self.__tail = new_node
            current_tail.next_node = new_node

        else:
            self.__head = self.__tail = new_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""

        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{node.data} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string
