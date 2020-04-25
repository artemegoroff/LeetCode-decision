import unittest
from main import Solution

s = Solution()


class SingleNumberTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(s.maxProfit([7, 1, 5, 3, 6, 4]), 7)

    def test2(self):
        self.assertEqual(s.maxProfit([1, 2, 3, 4, 5]), 4)

    def test3(self):
        self.assertEqual(s.maxProfit([7, 6, 4, 3, 1]), 0)
