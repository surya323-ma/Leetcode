You are given a 2D integer array intervals where intervals[i] = [starti, endi] represents all the integers from starti to endi inclusively.

A containing set is an array nums where each interval from intervals has at least two integers in nums.

For example, if intervals = [[1,3], [3,7], [8,9]], then [1,2,4,7,8,9] and [2,3,4,8,9] are containing sets.
Return the minimum possible size of a containing set.
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        res = []

        for start, end in intervals:
            count = 0
            for x in reversed(res):
                if x >= start and x <= end:
                    count += 1
                if count == 2:
                    break
            for i in range(2 - count):
                res.append(end - i)
        
        return len(res)
