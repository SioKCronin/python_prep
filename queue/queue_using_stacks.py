import unittest

class Stack(object):

    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop(0)

    def peek(self):
        return self._items[-1]

    def size(self):
        return len(self._items)

class QueueUsingStack():

    def __init__(self):
        # O(1)
        self.queue = Stack()

    def push(self, x):
        # O(1)
        return self.queue.push(x)

    def pop(self):
        # O(n)
        return self.queue.pop()

    def peek(self):
        # O(1)
        return self.queue.peek()

    def empty(self):
        # O(1)
        return self.queue.is_empty()

class TestQueueUsingStack(unittest.TestCase):

    def test_queue_setup(self):
        q = QueueUsingStack()
        self.assertIsInstance(q, QueueUsingStack)

    def test_push(self):
        q = QueueUsingStack()
        q.push(2)
        self.assertEqual(q.queue, [2])

    def test_pop(self):
        q = QueueUsingStack()
        q.push(2)
        q.push(3)
        self.assertEqual(q.pop(), 2)

    def test_peek(self):
        q = QueueUsingStack()
        q.push(2)
        q.push(3)
        self.assertEqual(q.peek(), 2)

    def test_empty(self):
        q = QueueUsingStack()
        q.push(2)
        q.push(3)
        self.assertFalse(q.empty())

if __name__ == '__main__':
    unittest.main()
