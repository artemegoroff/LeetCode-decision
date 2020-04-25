import unittest
from main import Solution

s = Solution()


class countElementsTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(s.backspaceCompare("ab#c", "ad#c"), True)

    def test2(self):
        self.assertEqual(s.backspaceCompare("ab##", "c#d#"), True)

    def test3(self):
        self.assertEqual(s.backspaceCompare("a#c", "b"), False)

    def test4(self):
        self.assertEqual(s.backspaceCompare("y#fo##f", "y#f#o##f"), True)



