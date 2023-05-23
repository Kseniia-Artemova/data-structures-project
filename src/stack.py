class Node:
    """Класс для узла стека"""

    def __init__(self, data: str, next_node=None) -> None:
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        :param next_node: ссылка на следующий объект стека, либо None
        """

        self.data = data
        self.__next_node = next_node

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        self.__next_node = next_node

    def __str__(self) -> str:
        """Возвращает данные объекта класса в виде строки"""

        return f"{self.data}"


class Stack:
    """Класс для стека"""

    def __init__(self) -> None:
        """
        Конструктор класса Stack

        :param items: список добавленных узлов
        :param top: ссылка на последний объект стека, либо None
        """

        self.__top = None

    @property
    def top(self) -> Node | None:
        return self.__top

    def __str__(self) -> str:
        """Возвращает информацию об узлах стека в формате строки"""

        if self.top is None:
            return ""

        nodes = ""
        node = self.top
        while node:
            nodes += node.data + "\n"
            node = node.next_node

        nodes = nodes.rstrip('\n')
        return f"Список узлов в стеке:\n{nodes}"

    def push(self, data: str) -> None:
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        node = Node(data)

        if self.top:
            node.next_node = self.top

        self.__top = node

    def pop(self) -> str:
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """

        if not self.top:
            raise IndexError("pop from empty list")
        else:
            node = self.top.data

            if not self.top.next_node:
                self.__top = None
            else:
                self.__top = self.top.next_node

            return node
