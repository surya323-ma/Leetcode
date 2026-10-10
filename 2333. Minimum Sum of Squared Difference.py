You are given two positive 0-indexed integer arrays nums1 and nums2, both of length n.

The sum of squared difference of arrays nums1 and nums2 is defined as the sum of (nums1[i] - nums2[i])2 for each 0 <= i < n.

You are also given two positive integers k1 and k2. You can modify any of the elements of nums1 by +1 or -1 at most k1 times. Similarly, you can modify any of the elements of nums2 by +1 or -1 at most k2 times.

Return the minimum sum of squared difference after modifying array nums1 at most k1 times and modifying array nums2 at most k2 times.

Note: You are allowed to modify the array elements to become negative integers.


from typing import List
from collections import Counter

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        k = k1 + k2
        cnt = Counter(abs(a - b) for a, b in zip(nums1, nums2))
        maxd = max(cnt)

        for d in range(maxd, 0, -1):
            if not k: break
            if cnt[d]:
                take = min(cnt[d], k)
                cnt[d] -= take
                cnt[d - 1] += take
                k -= take

        return sum(d * d * c for d, c in cnt.items())
