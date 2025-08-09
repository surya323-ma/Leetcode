You have two soups, A and B, each starting with n mL. On every turn, one of the following four serving operations is chosen at random, each with probability 0.25 independent of all previous turns:

pour 100 mL from type A and 0 mL from type B
pour 75 mL from type A and 25 mL from type B
pour 50 mL from type A and 50 mL from type B
pour 25 mL from type A and 75 mL from type B
Note:

There is no operation that pours 0 mL from A and 100 mL from B.
The amounts from A and B are poured simultaneously during the turn.
If an operation asks you to pour more than you have left of a soup, pour all that remains of that soup.
The process stops immediately after any turn in which one of the soups is used up.

class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4800:
            return 1.0

        units = (n + 24) // 25
        dp = [[0.0] * (units + 1) for _ in range(units + 1)]

        for a in range(units + 1):
            for b in range(units + 1):
                if a == 0 and b == 0:
                    dp[a][b] = 0.5
                elif a == 0:
                    dp[a][b] = 1.0
                elif b == 0:
                    dp[a][b] = 0.0
                else:
                    dp[a][b] = 0.25 * (
                        dp[max(0, a - 4)][b] +
                        dp[max(0, a - 3)][max(0, b - 1)] +
                        dp[max(0, a - 2)][max(0, b - 2)] +
                        dp[max(0, a - 1)][max(0, b - 3)]
                    )

        return dp[units][units]
