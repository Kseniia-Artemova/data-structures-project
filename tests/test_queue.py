"""Здесь надо написать тесты с использованием unittest для модуля queue."""

from src.queue import Queue
from src.queue import Node
import unittest


class TestNode(unittest.TestCase):

    def test_create_node(self):
        node = Node("data1")
        self.assertEqual(node.data, "data1")
        self.assertIsNone(node.next_node)

    def test_str_node(self):
        node = Node("data1")
        self.assertEqual(str(node), "data1")


class TestQueue(unittest.TestCase):

    def test_create_queue_empty(self):
        queue = Queue()
        self.assertIsNone(queue.head)
        self.assertIsNone(queue.tail)

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue("data1")
        self.assertEqual(queue.head.data, "data1")
        self.assertEqual(queue.tail.data, "data1")
        self.assertIsNone(queue.head.next_node)
        self.assertIsNone(queue.tail.next_node)

        queue.enqueue("data2")
        self.assertEqual(queue.head.data, "data1")
        self.assertEqual(queue.tail.data, "data2")
        self.assertEqual(queue.head.next_node.data, "data2")
        self.assertIsNone(queue.tail.next_node)

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue("data1")
        queue.enqueue("data2")
        queue.enqueue("data3")

        last = queue.dequeue()
        self.assertEqual(last, "data1")
        self.assertEqual(queue.head.data, "data2")
        self.assertEqual(queue.head.next_node.data, "data3")
        self.assertIsNone(queue.tail.next_node)

        last = queue.dequeue()
        self.assertEqual(last, "data2")
        self.assertEqual(queue.head.data, "data3")
        self.assertIsNone(queue.head.next_node)

        last = queue.dequeue()
        self.assertEqual(last, "data3")
        self.assertIsNone(queue.head)
        self.assertIsNone(queue.tail)

        last = queue.dequeue()
        self.assertIsNone(last)

    def test_str_empty(self):
        queue = Queue()
        self.assertEqual(str(queue), "")

    def test_str(self):
        queue = Queue()
        queue.enqueue("data1")
        queue.enqueue("data2")
        queue.enqueue("data3")

        self.assertEqual(str(queue), "data1\ndata2\ndata3")

