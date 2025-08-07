There is a game dungeon comprised of n x n rooms arranged in a grid.

You are given a 2D array fruits of size n x n, where fruits[i][j] represents the number of fruits in the room (i, j). Three children will play in the game dungeon, with initial positions at the corner rooms (0, 0), (0, n - 1), and (n - 1, 0).

The children will make exactly n - 1 moves according to the following rules to reach the room (n - 1, n - 1):

The child starting from (0, 0) must move from their current room (i, j) to one of the rooms (i + 1, j + 1), (i + 1, j), and (i, j + 1) if the target room exists.
The child starting from (0, n - 1) must move from their current room (i, j) to one of the rooms (i + 1, j - 1), (i + 1, j), and (i + 1, j + 1) if the target room exists.
The child starting from (n - 1, 0) must move from their current room (i, j) to one of the rooms (i - 1, j + 1), (i, j + 1), and (i + 1, j + 1) if the target room exists.
When a child enters a room, they will collect all the fruits there. If two or more children enter the same room, only one child will collect the fruits, and the room will be emptied after they leave.

Return the maximum number of fruits the children can collect from the dungeon.

from typing import List
import math

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        """
        Calculates the maximum fruits collected by three children using the three-region DP approach.
        """
        n = len(fruits)
        # Sum of three independent best-paths minus two extra counts of the final cell
        return (
            self.get_top_left(fruits)
            + self.get_top_right(fruits)
            + self.get_bottom_left(fruits)
            - 2 * fruits[n - 1][n - 1]
        )

    def get_top_left(self, fruits: List[List[int]]) -> int:
        """
        1) Straight diagonal from (0,0) to (n-1,n-1)
        """
        total = 0
        for i in range(len(fruits)):
            total += fruits[i][i]
        return total

    def get_top_right(self, fruits: List[List[int]]) -> int:
        """
        2) From (0,n-1) downwards through the upper-triangle region
        Allowed moves: down-left, down, down-right
        """
        n = len(fruits)
        # Initialize DP table with -infinity
        dp = [[float('-inf')] * n for _ in range(n)]
        dp[0][n - 1] = fruits[0][n - 1]

        dirs = [(1, -1), (1, 0), (1, 1)]  # (dx, dy)
        for x in range(n):
            for y in range(n):
                # Only process strictly above main diagonal region, plus end cell
                if x >= y and not (x == n - 1 and y == n - 1):
                    continue

                best_prev = float('-inf')
                for dx, dy in dirs:
                    px, py = x - dx, y - dy
                    if px < 0 or px >= n or py < 0 or py >= n:
                        continue
                    # Stay within the same triangular region
                    if px < py and py < (n - 1 - px):
                        continue
                    best_prev = max(best_prev, dp[px][py])

                # Update DP if valid predecessor found
                if best_prev > float('-inf'):
                    dp[x][y] = best_prev + fruits[x][y]

        return dp[n - 1][n - 1]

    def get_bottom_left(self, fruits: List[List[int]]) -> int:
        """
        3) From (n-1,0) rightwards through the lower-triangle region
        Allowed moves: up-right, right, down-right
        """
        n = len(fruits)
        # Initialize DP table with -infinity
        dp = [[float('-inf')] * n for _ in range(n)]
        dp[n - 1][0] = fruits[n - 1][0]

        dirs = [(-1, 1), (0, 1), (1, 1)]  # (dx, dy)
        for y in range(n):
            for x in range(n):
                # Only process strictly below main diagonal region, plus end cell
                if x <= y and not (x == n - 1 and y == n - 1):
                    continue

                best_prev = float('-inf')
                for dx, dy in dirs:
                    px, py = x - dx, y - dy
                    if px < 0 or px >= n or py < 0 or py >= n:
                        continue
                    # Stay within the same triangular region
                    if py < px and px < (n - 1 - py):
                        continue
                    best_prev = max(best_prev, dp[px][py])

                # Update DP if valid predecessor found
                if best_prev > float('-inf'):
                    dp[x][y] = best_prev + fruits[x][y]

        return dp[n - 1][n - 1]
