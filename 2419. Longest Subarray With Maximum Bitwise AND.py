You are given an integer array nums of size n.

Consider a non-empty subarray from nums that has the maximum possible bitwise AND.
In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
Return the length of the longest such subarray.
The bitwise AND of an array is the bitwise AND of all the numbers in it.
A subarray is a contiguous sequence of elements within an array.

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = max(nums)
        max_len = 0
        curr_len = 0
        for num in nums:
            if num == k:
                curr_len += 1
                max_len = max(max_len, curr_len)
            else:
                curr_len = 0

        return max_len    
