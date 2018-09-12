import unittest
import queue

class StackUsingQueue():

    def __init__(self):
        self.stack = queue.LifoQueue()

    def push(self, x):
        # O(1)
        self.stack.put(x)

    def pop(self):
        # O(1)
        return self.stack.get()

    def top(self):
        # O(2)
        val = self.stack.get()
        self.stack.put(val)
        return(val)

    def empty(self):
        # O(1)
        return self.stack.empty()


class TestStackUsingQueue(unittest.TestCase):

    def test_setup(self):
        s = StackUsingQueue()
        self.assertEqual(type(s), StackUsingQueue)

    def test_push(self):
        s = StackUsingQueue()
        s.push(2)
        self.assertFalse(s.empty())

    def test_pop(self):
        s = StackUsingQueue()
        s.push(2)
        self.assertEqual(s.pop(), 2)

    def test_top(self):
        s = StackUsingQueue()
        s.push(2)
        s.push(3)
        self.assertEqual(s.top(), 3)

    def test_empty(self):
        s = StackUsingQueue()
        self.assertTrue(s.empty())
        s.push(2)
        self.assertFalse(s.empty())

if __name__ == '__main__':
    unittest.main()
