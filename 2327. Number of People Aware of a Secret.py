On day 1, one person discovers a secret.
You are given an integer delay, which means that each person will share the secret with a new person every day, starting from delay days after discovering the secret. You are also given an integer forget, which means that each person will forget the secret forget days after discovering it. A person cannot share the secret on the same day they forgot it, or on any day afterwards
Given an integer n, return the number of people who know the secret at the end of day n. Since the answer may be very large, return it modulo 109 + 7.
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1 
        total = 0  
        for day in range(2, n + 1):
            share_start = day - delay
            forget_start = day - forget
            if share_start >= 1:
                total += dp[share_start]
            if forget_start >= 1:
                total -= dp[forget_start]
            dp[day] = total % MOD

        result = 0
        for day in range(n - forget + 1, n + 1):
            result = (result + dp[day]) % MOD

        return result
