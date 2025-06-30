We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

 class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_length = 0

        for num in count:
            if num + 1 in count:
                max_length = max(max_length, count[num] + count[num + 1])

        return max_length
