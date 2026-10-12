You are given a 0-indexed integer array nums and a positive integer k.

You can do the following operation on the array any number of times:

Choose any two distinct indices i and j and simultaneously update the values of nums[i] to (nums[i] AND nums[j]) and nums[j] to (nums[i] OR nums[j]). Here, OR denotes the bitwise OR operation, and AND denotes the bitwise AND operation.
You have to choose k elements from the final array and calculate the sum of their squares.

Return the maximum sum of squares you can achieve.

Since the answer can be very large, return it modulo 109 + 7.

from typing import List

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        cnt = [0]*30
        for x in nums:
            for i in range(30):
                if x >> i & 1:
                    cnt[i] += 1
        res = 0
        for _ in range(k):
            cur = 0
            for j in range(29, -1, -1):
                if cnt[j]:
                    cur |= 1 << j
                    cnt[j] -= 1
            res = (res + cur*cur) % MOD
        return res
