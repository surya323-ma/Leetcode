You are given a 0-indexed array nums consisiting of positive integers. You can do the following operation on the array any number of times:

Select an index i such that 0 <= i < n - 1 and replace either of nums[i] or nums[i+1] with their gcd value.
Return the minimum number of operations to make all elements of nums equal to 1. If it is impossible, return -1.

The gcd of two integers is the greatest common divisor of the two integers.
from math import gcd
from typing import List

class Solution:
  def minOperations(self, nums: list[int]) -> int:
    n = len(nums)
    ones = nums.count(1)
    if ones > 0:
      return n - ones
    minOps = math.inf

    for i, g in enumerate(nums):
      for j in range(i + 1, n):
        g = math.gcd(g, nums[j])
        if g == 1:   # gcd(nums[i..j]:== 1
          minOps = min(minOps, j - i)
          break
    return -1 if minOps == math.inf else minOps + n - 1
