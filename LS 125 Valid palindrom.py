class Solution:
    def isPalindrome(self, s: str) -> bool:
        rez = ''
        for i in s:
            if i.isalpha() or i.isdigit():
                rez += i
        return rez.lower() == rez[::-1].lower()