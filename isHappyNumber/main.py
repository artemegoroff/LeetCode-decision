class Solution:
    def isHappy(self, n: int) -> bool:
        kvadr = []

        while n != 1 and n not in kvadr:
            kvadr.append(n)
            s = 0
            for i in str(n):
                s += int(i) ** 2
            n = s
        return n==1
