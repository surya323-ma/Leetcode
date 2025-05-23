You are given an integer array nums of length n and a 2D array queries, where queries[i] = [li, ri].

For each queries[i]:

Select a subset of indices within the range [li, ri] in nums.
Decrement the values at the selected indices by 1.
A Zero Array is an array where all elements are equal to 0.

Return true if it is possible to transform nums into a Zero Array after processing all the queries sequentially, otherwise return false.
#code here
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n, m=len(nums), len(queries)
        freq=[0]*(n+1)
        for s, e in queries:
            freq[s]+=1
            freq[e+1]-=1
        op=0
        for i, x in enumerate(nums):
            op+=freq[i]
            if x>op: return False
        return True
