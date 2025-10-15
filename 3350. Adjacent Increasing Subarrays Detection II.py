Given an array nums of n integers, your task is to find the maximum value of k for which there exist two adjacent subarrays of length k each, such that both subarrays are strictly increasing. Specifically, check if there are two subarrays of length k starting at indices a and b (a < b), where:
Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
The subarrays must be adjacent, meaning b = a + k.
Return the maximum possible value of k.

A subarray is a contiguous non-empty sequence of elements within an array.
class Solution(object):
    def maxIncreasingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 1
        
        l = 0  # Last/previous sequence length
        c = 1  # Current sequence length
        m = 0  # Maximum k found
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                c += 1
            else:
                m = max(m, max(c//2, min(c, l)))
                l = c
                c = 1
        
        m = max(m, max(c//2, min(c, l)))
        return m
