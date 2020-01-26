import unittest
from LS_125 import Solution

s = Solution()

class PalindromTests(unittest.TestCase):

    def test1(self):
        self.assertEqual(s.isPalindrome('abrba'), True)

    def test2(self):
        self.assertEqual(s.isPalindrome('abrbar'), False)

    def test_3(self):
        self.assertEqual(s.isPalindrome(''), True)

    def test_4(self):
        self.assertEqual(s.isPalindrome('_a__'), True)

if __name__ =='main':
    unittest.main()

