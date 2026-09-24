You are given an integer array nums.
Return the smallest index i such that the sum of the digits of nums[i] is equal to i.
If no such index exists, return -1.

from typing import List

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            # compute digit sum using str conversion
            s = sum(int(d) for d in str(n))
            
            if s == i:
                return i
        return -1
