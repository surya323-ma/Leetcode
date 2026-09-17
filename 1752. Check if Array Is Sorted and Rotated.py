Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.
There may be duplicates in the original array.
Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.
class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        cnt=0
        for i in range(1,n):
            if nums[i-1]>nums[i]:
                cnt+=1
        if nums[0]<nums[n-1]:
            cnt+=1
        return cnt<=1
    
