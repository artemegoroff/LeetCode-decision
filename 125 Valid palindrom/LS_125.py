class Solution:
    def isPalindrome(self, s: str) -> bool:
        rez = ''
        for i in s:
            if i.isalpha() or i.isdigit():
                rez += i
        left=0
        right=len(rez)-1
        while left<right:
            if rez[left]!=rez[right]:
                return False
            left+=1
            right-=1
        return True