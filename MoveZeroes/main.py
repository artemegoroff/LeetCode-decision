from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_point = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[zero_point] = nums[i]
                zero_point += 1
        for i in range(zero_point, n):
            nums[i] = 0


s = Solution()
a = [0, 1, 0, 1, 0, 3, 12, 6, 43, 0, 32, 43, ]
s.moveZeroes(a)
print(a)
