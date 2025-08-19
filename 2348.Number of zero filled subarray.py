Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        length = 0
        for num in nums:
            if num == 0:
                length += 1
                count += length
            else:
                length = 0

        return count
