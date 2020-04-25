from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        def add(Heap, elem):
            Heap.append(elem)
            i = len(Heap) - 1
            while i > 1 and Heap[i // 2] < elem:
                Heap[i] = Heap[i // 2]
                i //= 2
                Heap[i] = elem

        def pop(Heap):
            if len(Heap) == 2:
                return Heap.pop()
            retval = Heap[1]
            Heap[1] = Heap.pop()
            i = 1
            while 2 * i + 1 < len(Heap) \
                    and Heap[i] < max(Heap[2 * i], Heap[2 * i + 1]):
                if Heap[2 * i] > Heap[2 * i + 1]:
                    Heap[i], Heap[2 * i] = Heap[2 * i], Heap[i]
                    i = 2 * i
                else:
                    Heap[i], Heap[2 * i + 1] = Heap[2 * i + 1], Heap[i]
                    i = 2 * i + 1
            if 2 * i == len(Heap) - 1 and Heap[i] < Heap[2 * i]:
                Heap[i], Heap[2 * i] = Heap[2 * i], Heap[i]
            return retval

        heap = [None]
        for stone in stones:
            add(heap, stone)
            # print(heap)
        while len(heap) > 2:
            one = pop(heap)
            second = pop(heap)
            if one != second:
                add(heap, abs(one - second))
        return heap[1] if len(heap)==2 else 0

s = Solution()
print(s.lastStoneWeight([2, 7, 4, 1, 8, 1]))

