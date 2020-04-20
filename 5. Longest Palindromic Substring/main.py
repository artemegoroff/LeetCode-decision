
class Solution:

    def find_longest_palindrom(self,s,left, right):
        n = len(s)
        while left>=0 and right<n and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]

    def longestPalindrome(self, s: str) -> str:

        rez = ''
        for i in range(len(s)):
            odd = self.find_longest_palindrom(s,i-1,i+1)
            even = self.find_longest_palindrom(s,i,i+1)
            rez = max(rez, odd, even, key=len)
        return rez

obj = Solution()
print(obj.longestPalindrome('babad'))

