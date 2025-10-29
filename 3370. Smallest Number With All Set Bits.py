You are given a positive number n.
Return the smallest number x greater than or equal to n, such that the binary representation of x contains only set bits
class Solution:
    def smallestNumber(self, n: int) -> int:
        x = 1
        while x < n:
            x = (x << 1) | 1  # Shift left and set the lowest bit
        return x
    
