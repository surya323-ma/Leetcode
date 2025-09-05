You are given two integers num1 and num2.

In one operation, you can choose integer i in the range [0, 60] and subtract 2i + num2 from num1.

Return the integer denoting the minimum number of operations needed to make num1 equal to 0.

If it is impossible to make num1 equal to 0, return -1.
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for t in range(1, 61):   
            s = num1 - t * num2
            if s < t:
                continue
            if s.bit_count() <= t:
                return t
        return -1

 
