import unittest
from main import Solution

s = Solution()

class SingleNumberTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(s.singleNumber([2,2,1]), 1)

    def test2(self):
        self.assertEqual(s.singleNumber([4,1,2,1,2]), 4)