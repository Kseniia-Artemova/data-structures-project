"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack
from src.stack import Node


class TestNode(unittest.TestCase):

    def test_data_Node(self):
        node = Node("data")
        self.assertEqual(node.data, "data")
        self.assertIsNone(node.next_node)

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

        self.assertIsInstance(stack.pop(), Node)
        self.assertEqual(len(stack.items), 1)
        
        self.assertIsInstance(stack.pop(), Node)
        self.assertEqual(stack.items, [])

        with self.assertRaises(IndexError):
            stack.pop()

