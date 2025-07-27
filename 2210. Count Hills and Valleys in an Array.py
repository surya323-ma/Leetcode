You are given a 0-indexed integer array nums. An index i is part of a hill in nums if the closest non-equal neighbors of i are smaller than nums[i]. Similarly, an index i is part of a valley in nums if the closest non-equal neighbors of i are larger than nums[i]. Adjacent indices i and j are part of the same hill or valley if nums[i] == nums[j].

Note that for an index to be part of a hill or valley, it must have a non-equal neighbor on both the left and right of the index.

Return the number of hills and valleys in nums.


                                                     class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(1, n - 1):
            if nums[i] == nums[i - 1]:
                continue
            left = i - 1
            while left >= 0 and nums[left] == nums[i]:
                left -= 1
            right = i + 1
            while right < n and nums[right] == nums[i]:
                right += 1
            if left >= 0 and right < n:
                if nums[i] > nums[left] and nums[i] > nums[right]:
                    count += 1  # Hill
                elif nums[i] < nums[left] and nums[i] < nums[right]:
                    count += 1 

        return count
