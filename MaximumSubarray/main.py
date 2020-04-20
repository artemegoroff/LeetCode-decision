from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = nums[0]
        left = 0
        right = 0
        curr_s = 0
        negative_pos = -1
        for i in range(len(nums)):
            curr_s += nums[i]

            if curr_s > best_sum:
                best_sum = curr_s
                left = negative_pos + 1
                right = i + 1


            if curr_s < 0:
                negative_pos = i
                curr_s = 0
        return best_sum
