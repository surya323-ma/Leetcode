Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_val = nums[0]
        res = -1
        for j in range(1, len(nums)):
            if nums[j] > min_val:
                res = max(res, nums[j] - min_val)
            min_val = min(min_val, nums[j])
        return res
