import unittest
from main import Solution

s = Solution()


class countElementsTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(s.countElements([1,2,3]), 2)

    def test2(self):
        self.assertEqual(s.countElements([1,1,3,3,5,5,7,7]), 0)

    def test3(self):
        self.assertEqual(s.countElements([1,1,2,2]), 2)
