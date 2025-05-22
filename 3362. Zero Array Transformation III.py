You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri].

Each queries[i] represents the following action on nums:

Decrement the value at each index in the range [li, ri] in nums by at most 1.
The amount by which the value is decremented can be chosen independently for each index.
A Zero Array is an array with all its elements equal to 0.

Return the maximum number of elements that can be removed from queries, such that nums can still be converted to a zero array using the remaining queries. If it is not possible to convert nums to a zero array, return -1.
#code here
from collections import deque
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        q= deque(sorted(queries))
        h = []
        selected =[]
        ans = 0
        # print(q)
        for i in range(len(nums)):
            while q and q[0][0] <= i:
                heapq.heappush(h,-q.popleft()[1])
            while selected and selected[0]<i:
                heapq.heappop(selected)

            while nums[i] > len(selected):
                if h and -h[0] >= i:
                    # print(-h[0],i)
                    heapq.heappush(selected,-heapq.heappop(h))
                    
                    ans += 1
                else:
                    return -1

        return len(queries)-ans
