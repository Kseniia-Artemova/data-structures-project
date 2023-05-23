"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack
from src.stack import Node


class TestNode(unittest.TestCase):

    def test_data_Node(self):
        node = Node("data")
        self.assertEqual(node.data, "data")
        self.assertIsNone(node.next_node)
        self.assertEqual(str(node), "data")


class TestStack(unittest.TestCase):

    def test_data_Stack_empty(self):
        stack = Stack()
        self.assertIsNone(stack.top)

    def test_push_Stack(self):
        stack = Stack()

        stack.push("data1")
        self.assertIsNotNone(stack.top)
        self.assertEqual(stack.top.data, "data1")
        self.assertIsNone(stack.top.next_node)

        stack.push("data2")
        self.assertEqual(stack.top.data, "data2")
        self.assertEqual(stack.top.next_node.data, "data1")

    def test_pop_Stack(self):
        stack = Stack()
        stack.push("data1")
        stack.push("data2")
        stack.push("data3")

        self.assertEqual(stack.pop(), "data3")
        self.assertEqual(stack.top.data, "data2")
        self.assertEqual(stack.top.next_node.data, "data1")

        self.assertEqual(stack.pop(), "data2")
        self.assertEqual(stack.top.data, "data1")
        self.assertIsNone(stack.top.next_node)

        self.assertEqual(stack.pop(), "data1")
        self.assertIsNone(stack.top)

        with self.assertRaises(IndexError):
            stack.pop()

    def test_str_empty(self):
        stack = Stack()
        self.assertEqual(str(stack), "")

    def test_str_two_nodes(self):
        stack = Stack()
        stack.push("data1")
        stack.push("data2")
        result = "Список узлов в стеке:\ndata2\ndata1"
        self.assertEqual(str(stack), result)
