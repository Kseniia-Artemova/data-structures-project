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

    def test_to_list(self):
        link_list = LinkedList()

        link_list.insert_beginning({'id': 2})
        link_list.insert_beginning({'id': 1})
        link_list.insert_beginning({'id': 0})
        link_list.insert_at_end({'id': 3})
        link_list.insert_at_end({'id': 4})

        self.assertEqual(len(link_list.to_list()), 5)
        lst = [{'id': 0}, {'id': 1}, {'id': 2}, {'id': 3}, {'id': 4}]
        self.assertEqual(link_list.to_list(), lst)

    def test_get_data_by_id(self):
        link_list = LinkedList()

        link_list.insert_beginning({'id': 2})
        link_list.insert_beginning({'id': 1})
        link_list.insert_beginning({'id': 0})
        link_list.insert_at_end({'id': 3})
        link_list.insert_at_end({'id': 4})

        self.assertEqual(link_list.get_data_by_id(0), {'id': 0})
        self.assertEqual(link_list.get_data_by_id(3), {'id': 3})
        self.assertIsNone(link_list.get_data_by_id(6))

        link_list.insert_beginning({"data"})
        self.assertRaises(TypeError, link_list.get_data_by_id(0))
        link_list.insert_at_end({'id': "5"})
        self.assertRaises(TypeError, link_list.get_data_by_id(5))
        self.assertIsNone(link_list.get_data_by_id(5))





