You are given a 0-indexed integer array nums and two integers key and k. A k-distant index is an index i of nums for which there exists at least one index j such that |i - j| <= k and nums[j] == key.

Return a list of all k-distant indices sorted in increasing order.
#code here
from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_indices = [i for i, val in enumerate(nums) if val == key]
        result = [] 
        for i in range(len(nums)):
            for j in key_indices:
                if abs(i - j) <= k:
                    result.append(i)
                    break 
        return result
