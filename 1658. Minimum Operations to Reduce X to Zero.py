You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.
Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

 

from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target, n = sum(nums) - x, len(nums)
        if target == 0: return n

        cur = left = max_len = 0
        for right, val in enumerate(nums):
            cur += val
            while left <= right and cur > target:
                cur -= nums[left]; left += 1
            if cur == target:
                max_len = max(max_len, right - left + 1)

        return n - max_len if max_len else -1
