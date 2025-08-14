Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for x in nums:
            freq[x]=freq.get(x,0)+1
        heap=[(-val,key)for key,val in freq.items()]
        heapq.heapify(heap)
        ans=[]
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
