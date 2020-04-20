import unittest
from main import Solution

s = Solution()

class SingleNumberTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(s.isHappy(19), True)

    def test2(self):
        self.assertEqual(s.isHappy(45), True)

