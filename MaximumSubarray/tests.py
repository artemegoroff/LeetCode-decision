import unittest
from main import Solution

s = Solution()

class MaxSubArrayTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)

    def test2(self):
        self.assertEqual(s.maxSubArray([-1]), -1)

