"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack
from src.stack import Node


class TestNode(unittest.TestCase):

    def test_data_Node(self):
        node = Node("data")
        self.assertEqual(node.data, "data")
        self.assertIsNone(node.next_node)


class TestStack(unittest.TestCase):

    def test_data_Stack(self):
        stack = Stack()
        self.assertEqual(stack.items, [])
        self.assertIsNone(stack.top)

    def test_push_Stack(self):
        stack = Stack()
        stack.push("data1")
        self.assertEqual(len(stack.items), 1)
        self.assertIsNotNone(stack.top)
        stack.push("data2")
        self.assertEqual(len(stack.items), 2)
        self.assertIsNotNone(stack.top)

    def test_pop_Stack(self):
        stack = Stack()
        stack.push("data1")
        stack.push("data2")
        self.assertEqual(len(stack.items), 2)

        self.assertEqual(stack.pop(), "data2")
        self.assertEqual(len(stack.items), 1)
        self.assertEqual(stack.top.data, "data1")

        self.assertEqual(stack.pop(), "data1")
        self.assertEqual(stack.items, [])
        self.assertIsNone(stack.top)

        with self.assertRaises(IndexError):
            stack.pop()

    def test_str_empty(self):
        stack = Stack()
        result = f"Объект стека. Список узлов:{''}\nПоследний добавленный узел: {None}"
        self.assertEqual(str(stack), result)

    def test_str_two_nodes(self):
        stack = Stack()
        stack.push("data1")
        stack.push("data2")
        result = f"Объект стека. Список узлов:\n" \
                 f"data1\ndata2\n" \
                 f"Последний добавленный узел: data2"
        self.assertEqual(str(stack), result)
