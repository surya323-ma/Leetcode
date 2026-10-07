Given a string s, calculate its reverse degree.

The reverse degree is calculated as follows:

For each character, multiply its position in the reversed alphabet ('a' = 26, 'b' = 25, ..., 'z' = 1) with its position in the string (1-indexed).
Sum these products for all characters in the string.
Return the reverse degree of s.

class Solution:
    def reverseDegree(self, s: str) -> int:
        sum=0
        for i in range(len(s)):
            idx=ord('z')-ord(s[i])+1
            sum=sum+(idx*(i+1))

        return sum
