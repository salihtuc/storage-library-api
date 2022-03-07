import unittest
from .stack_impl import Stack, NullElementException, EmptyStackException
from random import randint


class TestBasics(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_base_emptiness(self):
        self.assertEqual(self.stack.empty(), True)

    def test_base_size(self):
        self.assertEqual(self.stack.size(), 0)

    def test_base_pushing_null(self):
        self.assertRaises(NullElementException, lambda: self.stack.push(None))

    def test_base_peek(self):
        self.assertRaises(EmptyStackException, lambda: self.stack.peek())

    def test_base_pop(self):
        self.assertRaises(EmptyStackException, lambda: self.stack.pop())

    def test_base_pushing_one(self):
        self.stack.push("First item")
        self.assertEqual(self.stack.size(), 1)
        self.assertEqual(self.stack.peek(), 'First item')


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        self.stack.push("First item")

    def test_pushing_some(self):
        size_before = self.stack.size()
        random_iter_size = randint(1, 100)
        size_target = size_before + random_iter_size

        for i in range(random_iter_size):
            self.stack.push(i)

        self.assertEqual(self.stack.size(), size_target)

    def test_peek(self):
        top = self.stack.peek()
        self.assertEqual(top, "First item")
        self.assertEqual(self.stack.empty(), False)
        self.assertEqual(self.stack.size(), 1)

    def test_pop(self):
        top = self.stack.pop()
        self.assertEqual(top, "First item")
        self.assertEqual(self.stack.empty(), True)
        self.assertEqual(self.stack.size(), 0)

    def test_mix_push(self):
        self.stack.push("Second item")

        # First Peek & Pop
        self.assertEqual(self.stack.size(), 2)
        self.assertEqual(self.stack.empty(), False)
        self.assertEqual(self.stack.peek(), "Second item")
        self.assertEqual(self.stack.pop(), "Second item")
        self.assertEqual(self.stack.size(), 1)

        # Second Peek & Pop
        self.assertEqual(self.stack.empty(), False)
        self.assertEqual(self.stack.peek(), "First item")
        self.assertEqual(self.stack.pop(), "First item")
        self.assertEqual(self.stack.size(), 0)

        # Third Peek & Pop (fail)
        self.assertEqual(self.stack.empty(), True)
        self.assertRaises(EmptyStackException, lambda: self.stack.peek())
        self.assertRaises(EmptyStackException, lambda: self.stack.pop())
