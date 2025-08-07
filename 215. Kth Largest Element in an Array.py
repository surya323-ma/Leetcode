Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Step 1: Build a min-heap with the first k elements
        heap = nums[:k]
        heapq.heapify(heap)

        # Step 2: Iterate through the remaining elements
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)

        # Step 3: The root of the heap is the Kth largest
        return heap[0]
