You are given a 2D integer array intervals, where intervals[i] = [li, ri, weighti]. Interval i starts at position li and ends at ri, and has a weight of weighti. You can choose up to 4 non-overlapping intervals. The score of the chosen intervals is defined as the total sum of their weights.
Return the lexicographically smallest array of at most 4 indices from intervals with maximum score, representing your choice of non-overlapping intervals.
Two intervals are said to be non-overlapping if they do not share any points. In particular, intervals sharing a left or right boundary are considered overlapping.
import bisect
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        arr = sorted([(s,e,w,i) for i,(s,e,w) in enumerate(intervals)])
        starts = [s for s,_,_,_ in arr]
        n = len(arr)
        dp = [[(0,[])]*5 for _ in range(n+1)]

        for i in range(n-1,-1,-1):
            s,e,w,idx = arr[i]
            nxt = bisect.bisect_right(starts,e)
            for c in range(1,5):
                skip_w,skip_seq = dp[i+1][c]
                take_w,take_seq = dp[nxt][c-1]
                cand_w,cand_seq = take_w+w, sorted(take_seq+[idx])
                dp[i][c] = (cand_w,cand_seq) if cand_w>skip_w or (cand_w==skip_w and cand_seq<skip_seq) else (skip_w,skip_seq)
        return dp[0][4][1]


 
