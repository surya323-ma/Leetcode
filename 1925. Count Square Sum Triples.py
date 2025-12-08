A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.

Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.

class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n+1):
            for b in range(1, n+1):
                c2 = a*a + b*b
                c = int(c2**0.5)
                if c*c == c2 and c <= n:
                    count += 1
        return count
