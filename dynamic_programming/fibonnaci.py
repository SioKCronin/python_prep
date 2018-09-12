import unittest
from collections import defaultdict

class TestFibonnaci(unittest.TestCase):

    def test_recursive(self):
        self.assertEqual(nth_fibonnaci_recursive(5), 5)
        self.assertEqual(nth_fibonnaci_recursive(10), 55)

    def test_topdown_dp(self):
        self.assertEqual(topdown_dp_fibonnaci(5, [0]*6), 5)
        self.assertEqual(topdown_dp_fibonnaci(10, [0]*11), 55)

    def test_bottom_up_dp(self):
        self.assertEqual(bottom_up_dp_fibonnaci(5), 5)
        self.assertEqual(bottom_up_dp_fibonnaci(10), 55)

def nth_fibonnaci_recursive(n):
    if n <= 0: return 0
    if n == 1: return 1
    else:
        return nth_fibonnaci_recursive(n-1) + nth_fibonnaci_recursive(n-2)

def topdown_dp_fibonnaci(n, memo):
    if n == 0 or n == 1: return n
    if memo[n] == 0:
        memo[n] = topdown_dp_fibonnaci(n-1, memo) + topdown_dp_fibonnaci(n-2, memo)
    return memo[n]

def bottom_up_dp_fibonnaci(n):
    if n == 0: return 0
    a, b = 0, 1
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    return a + b

if __name__ == '__main__':
    unittest.main()
