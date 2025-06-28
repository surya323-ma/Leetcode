You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 import heapq

class Solution(object):
    def maxSubsequence(self, nums, k):
        heap = []
        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i))
            if len(heap) > k:
                heapq.heappop(heap)
        indices = sorted([idx for _, idx in heap])
        return [nums[i] for i in indices]
