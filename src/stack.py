class Node:
    """Класс для узла стека"""

    def __init__(self, data: str) -> None:
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        :param next_node: ссылка на следующий объект стека, либо None
        """

        self.data = data
        self.__next_node = None

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        self.__next_node = next_node

    def __str__(self) -> str:
        return f"{self.data}"


class Stack:
    """Класс для стека"""

    def __init__(self) -> None:
        """
        Конструктор класса Stack

        :param items: список добавленных узлов
        :param top: ссылка на последний объект стека, либо None
        """
        self.__items = []
        self.__top = None

    @property
    def items(self) -> list:
        return self.__items

    @property
    def top(self) -> Node | None:
        return self.__top

    def __str__(self) -> str:
        return "Объект стека. Список узлов:\n" + \
                "".join([item.data + "\n" for item in self.items]) + \
                f"Последний добавленный узел: {self.top}"

    def push(self, data: str) -> None:
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        data_node = Node(data)

        if self.__items:
            data_node.next_node = self.__items[-1]

        self.__items.append(data_node)
        self.__top = data_node

    def pop(self) -> str | None:
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if self.__items:
            last_item = self.__items.pop()
            self.__top = self.__items[-1] if self.__items else None
            return last_item.data
        else:
            raise IndexError("pop from empty list")
