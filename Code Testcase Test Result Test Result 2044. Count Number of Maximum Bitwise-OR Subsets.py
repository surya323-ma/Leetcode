Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.

The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).

from functools import lru_cache
from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num

        @lru_cache(maxsize=None)
        def dfs(index, current_or):
            if index == len(nums):
                return 1 if current_or == max_or else 0
            # Count subsets including and excluding current element
            include = dfs(index + 1, current_or | nums[index])
            exclude = dfs(index + 1, current_or)
            return include + exclude

        return dfs(0, 0)
 
