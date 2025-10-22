You are given an integer array nums and two integers k and numOperations.

You must perform an operation numOperations times on nums, where in each operation you:

Select an index i that was not selected in any previous operations.
Add an integer in the range [-k, k] to nums[i].
Return the maximum possible frequency of any element in nums after performing the operations.
from collections import Counter
from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def maxFrequency(self, a: List[int], k: int, op: int) -> int:
        a.sort()
        count = Counter(a)
        max_freq = 0

        for i, v in enumerate(a):
            # Count of elements within [v - k, v + k] excluding current frequency
            nearby = bisect_right(a, v + k) - bisect_left(a, v - k) - count[v]
            # Option 1: Use up to op operations to boost frequency of v
            freq1 = min(nearby, op) + count[v]
            # Option 2: Use op operations to bring elements to v + 2k
            freq2 = min(bisect_right(a, v + 2 * k) - i, op)
            max_freq = max(max_freq, freq1, freq2)

        return max_freq
