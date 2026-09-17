You are given an array of integers arr and an integer target.
You have to find two non-overlapping sub-arrays of arr each with a sum equal target. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.
Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.
from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        prefix = {0: -1}   # sum -> index
        s = 0
        best = [float('inf')] * n
        ans = float('inf')
        
        for i, x in enumerate(arr):
            s += x
            if (s - target) in prefix:
                l = prefix[s - target] + 1
                length = i - l + 1
                if l > 0:
                    ans = min(ans, length + best[l-1])
                best[i] = min(best[i-1] if i > 0 else float('inf'), length)
            else:
                best[i] = best[i-1] if i > 0 else float('inf')
            prefix[s] = i
        
        return -1 if ans == float('inf') else ans
