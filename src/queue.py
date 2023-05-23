class Node:
    """Класс для узла очереди"""

    def __init__(self, data: str, next_node=None) -> None:
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """

        self.data = data
        self.__next_node = next_node

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node) -> None:
        self.__next_node = next_node

    def __str__(self) -> str:
        """Возвращает строку data класса в формате строки"""

        return f"{self.data}"


class Queue:
    """Класс для очереди"""

    def __init__(self) -> None:
        """Конструктор класса Queue"""

        self.__head = None
        self.__tail = None

    @property
    def head(self) -> Node | None:
        return self.__head

    @property
    def tail(self) -> Node | None:
        return self.__tail

    def enqueue(self, data: str) -> None:
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """

        node = Node(data)

        if self.head is None:
            self.__head = node
        else:
            self.tail.next_node = node

        self.__tail = node

    def dequeue(self) -> str | Exception:
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """

        if self.head is None:
            raise IndexError("Очередь пуста")

        else:
            node = self.head.data

            if self.head.next_node is None:
                self.__tail = self.__head = None
            else:
                self.__head = self.head.next_node

            return node

    def __str__(self) -> str:
        """Магический метод для строкового представления объекта"""

        if self.head is None:
            return ""

        nodes = ""
        node = self.head
        while node:
            nodes += node.data + "\n"
            node = node.next_node

        return nodes.rstrip("\n")
