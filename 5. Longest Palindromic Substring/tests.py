import unittest
from main import Solution

s = Solution()

class LongPalindromTests(unittest.TestCase):

    def test1(self):
        self.assertEqual(s.longestPalindrome('babad'), 'aba')

    def test2(self):
        self.assertEqual(s.longestPalindrome('cbbd'), 'bb')

    def test_3(self):
        self.assertEqual(s.longestPalindrome('abrararb'), 'brararb')

    def test_4(self):
        self.assertEqual(s.longestPalindrome('aaaaaa'), 'aaaaaa')

if __name__ =='main':
    unittest.main()

