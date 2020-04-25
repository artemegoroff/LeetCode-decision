from typing import List
from collections import Counter


class Solution:
    def countElements(self, arr: List[int]) -> int:

        d = Counter(arr)
        count = 0
        for key in d:
            if key + 1 in d:
                count += min(d[key], d[key + 1])
        return count
