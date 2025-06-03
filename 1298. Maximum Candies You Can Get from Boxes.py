You have n boxes labeled from 0 to n - 1. You are given four arrays: status, candies, keys, and containedBoxes where:

status[i] is 1 if the ith box is open and 0 if the ith box is closed,
candies[i] is the number of candies in the ith box,
keys[i] is a list of the labels of the boxes you can open after opening the ith box.
containedBoxes[i] is a list of the boxes you found inside the ith box.
You are given an integer array initialBoxes that contains the labels of the boxes you initially have. You can take all the candies in any open box and you can use the keys in it to open new boxes and you also can use the boxes you find in it.

Return the maximum number of candies you can get following the rules above.
#code here
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        res = 0
        q = deque(initialBoxes)
        visit = set()
        while q:
            for i in range(len(q)):
                curBox = q.popleft()
                if curBox in visit:
                    continue
                visit.add(curBox)
                
                if status[curBox]:
                    res += candies[curBox]
                    # Update status and/or reset visit and q if already visited
                    for k in keys[curBox]:
                        if k in visit and status[k] == 0:
                            status[k] = 1
                            q.append(k)
                            visit.remove(k)
                        else:
                            status[k] = 1
                    # add boxes found in current box to q
                    for box in containedBoxes[curBox]:
                        q.append(box)
        return res
