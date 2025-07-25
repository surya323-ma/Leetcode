You are given an integer array nums.

You are allowed to delete any number of elements from nums without making it empty. After performing the deletions, select a subarray of nums such that:

All elements in the subarray are unique.
The sum of the elements in the subarray is maximized.
Return the maximum sum of such a subarray.

class Solution:
    def maxSum(self, nums):
        used = set()
        total_sum = max_element = float('-inf')

        for num in nums:
            max_element = max(max_element, num)
            if num > 0 and num not in used:
                total_sum += num
                used.add(num)

        return total_sum if total_sum > float('-inf') else max_element
