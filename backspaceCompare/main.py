from typing import List
from collections import Counter


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        def deleteSpace(s):
            stack = []
            n = len(s)
            for i in s:
                if i == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(i)
            return ''.join(stack)

        s = deleteSpace(S)
        t = deleteSpace(T)
        return s == t
