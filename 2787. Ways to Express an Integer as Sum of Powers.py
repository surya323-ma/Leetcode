Given two positive integers n and x.

Return the number of ways n can be expressed as the sum of the xth power of unique positive integers, in other words, the number of sets of unique integers [n1, n2, ..., nk] where n = n1x + n2x + ... + nkx.

Since the result can be very large, return it modulo 109 + 7.

For example, if n = 160 and x = 3, one way to express n is n = 23 + 33 + 53.
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        if n == 1:
            return 1
        MOD = 10**9+7
        p = [0] * (n+1)
        p[0] = 1

        for i in range(1, n+1):
            b = i**x
            if b > n:
                break
            for j in range(n, b-1, -1):
                p[j] += p[j-b]

        return p[-1]%MOD
