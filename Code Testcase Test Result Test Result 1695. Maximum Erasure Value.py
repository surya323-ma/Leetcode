You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        last_seen = [0] * 10001 
        left = 0
        max_sum = 0
        for right in range(1, n + 1):
            val = nums[right - 1]
            left = max(left, last_seen[val])
            max_sum = max(max_sum, prefix_sum[right] - prefix_sum[left])
            last_seen[val] = right
        return max_sum
