import unittest
import time

class TestCoinChange(unittest.TestCase):

    def test_leet1(self):
        self.assertEqual(dp_coin_changer([1, 2, 5], 11, 2), 3)
        self.assertEqual(dp_coin_changer([2], 3, 0), -1)

def dp_coin_changer(coin_value_list, change, i, memo=[]):
    if i == -1:
        return -1

    memo.append(coin_value_list[i])
    s = round(sum(memo), 2)

    if s < change:
        return dp_coin_changer(coin_value_list, change, i, memo)

    if s > change:
        memo.pop()
        i -= 1
        return dp_coin_changer(coin_value_list, change, i, memo)

    return len(memo)

if __name__ == '__main__':
    unittest.main()
