"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import Node, LinkedList


class TestNode(unittest.TestCase):

    def test_create_node(self):
        node = Node({'id': 1})
        self.assertEqual(node.data, {'id': 1})
        self.assertIsNone(node.next_node)

    def test_str_node(self):
        node = Node({'id': 4})
        self.assertEqual(str(node), "{'id': 4}")


class TestLinkedList(unittest.TestCase):

    def test_create_linkedlist(self):
        link_list = LinkedList()
        self.assertIsNone(link_list.head)
        self.assertIsNone(link_list.tail)

    def test_insert_beginning(self):
        link_list = LinkedList()

        link_list.insert_beginning({'id': 1})
        self.assertEqual(link_list.head.data, {'id': 1})
        self.assertEqual(link_list.tail.data, {'id': 1})

        link_list.insert_beginning({'id': 2})
        self.assertEqual(link_list.head.data, {'id': 2})
        self.assertEqual(link_list.head.next_node.data, {'id': 1})
        self.assertEqual(link_list.tail.data, {'id': 1})
        self.assertIsNone(link_list.tail.next_node)

        link_list.insert_beginning({'id': 3})
        self.assertEqual(link_list.head.data, {'id': 3})
        self.assertEqual(link_list.head.next_node.data, {'id': 2})
        self.assertEqual(link_list.tail.data, {'id': 1})
        self.assertIsNone(link_list.tail.next_node)

    def test_insert_at_end(self):
        link_list = LinkedList()

        link_list.insert_at_end({'id': 1})
        self.assertEqual(link_list.tail.data, {'id': 1})
        self.assertEqual(link_list.head.data, {'id': 1})
        self.assertIsNone(link_list.tail.next_node)

        link_list.insert_at_end({'id': 2})
        self.assertEqual(link_list.tail.data, {'id': 2})
        self.assertEqual(link_list.head.data, {'id': 1})
        self.assertIsNone(link_list.tail.next_node)

        link_list.insert_at_end({'id': 3})
        self.assertEqual(link_list.tail.data, {'id': 3})
        self.assertEqual(link_list.head.data, {'id': 1})
        self.assertIsNone(link_list.tail.next_node)

    def test_str_linkedlist(self):
        link_list = LinkedList()

        self.assertEqual(str(link_list), "None")

        link_list.insert_beginning({'id': 2})
        link_list.insert_beginning({'id': 1})
        link_list.insert_beginning({'id': 0})
        link_list.insert_at_end({'id': 3})
        link_list.insert_at_end({'id': 4})

        expection = "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> {'id': 4} -> None"
        self.assertEqual(str(link_list), expection)



