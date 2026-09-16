Given n points on a 1-D plane, where the ith point (from 0 to n-1) is at x = i, find the number of ways we can draw exactly k non-overlapping line segments such that each segment covers two or more points. The endpoints of each segment must have integral coordinates. The k line segments do not have to cover all n points, and they are allowed to share endpoints.

Return the number of ways we can draw k non-overlapping line segments. Since this number can be huge, return it modulo 109 + 7.
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (k+1) for _ in range(n)]
        prefix = [[0] * (k+1) for _ in range(n)]
        
        for i in range(n):
            dp[i][0] = 1
            prefix[i][0] = (prefix[i-1][0] if i > 0 else 0) + dp[i][0]
        
        for i in range(1, n):
            for j in range(1, k+1):
                dp[i][j] = (dp[i-1][j] + prefix[i-1][j-1]) % MOD
                prefix[i][j] = (prefix[i-1][j] + dp[i][j]) % MOD
        
        return dp[n-1][k]
