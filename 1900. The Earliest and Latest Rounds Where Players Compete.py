There is a tournament where n players are participating. The players are standing in a single row and are numbered from 1 to n based on their initial standing position (player 1 is the first player in the row, player 2 is the second player in the row, etc.).

The tournament consists of multiple rounds (starting from round number 1). In each round, the ith player from the front of the row competes against the ith player from the end of the row, and the winner advances to the next round. When the number of players is odd for the current round, the player in the middle automatically advances to the next round.

For example, if the row consists of players 1, 2, 4, 6, 7
Player 1 competes against player 7.
Player 2 competes against player 6.
Player 4 automatically advances to the next round.
After each round is over, the winners are lined back up in the row based on the original ordering assigned to them initially (ascending order).

The players numbered firstPlayer and secondPlayer are the best in the tournament. They can win against any other player before they compete against each other. If any two other players compete against each other, either of them might win, and thus you may choose the outcome of this round.

Given the integers n, firstPlayer, and secondPlayer, return an integer array containing two values, the earliest possible round number and the latest possible round number in which these two players will compete against each other, respectively.

from functools import lru_cache

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> list[int]:
        @lru_cache(None)
        def dfs(n, p1, p2):
            if p1 + p2 == n + 1:
                return (1, 1)
            if p1 > p2:
                p1, p2 = p2, p1
            if n <= 4:
                return (2, 2)

            m = (n + 1) // 2
            minR, maxR = float('inf'), float('-inf')
            if p1 - 1 > n - p2:
                p1, p2 = n + 1 - p2, n + 1 - p1
            if p2 * 2 <= n + 1:
                for i in range(p1):
                    for j in range(p2 - p1 - 1 + 1):
                        r1, r2 = dfs(m, i + 1, i + j + 2)
                        minR = min(minR, r1 + 1)
                        maxR = max(maxR, r2 + 1)
            else:
                p4 = n + 1 - p2
                for i in range(p1):
                    for j in range(p4 - p1 - 1 + 1):
                        offset = i + j + 1 + ((p2 - p4 - 1 + 1) // 2) + 1
                        r1, r2 = dfs(m, i + 1, offset)
                        minR = min(minR, r1 + 1)
                        maxR = max(maxR, r2 + 1)

            return (minR, maxR)

        return list(dfs(n, firstPlayer, secondPlayer))
