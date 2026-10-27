You are given an m x n matrix grid and a positive integer k. An island is a group of positive integers (representing land) that are 4-directionally connected (horizontally or vertically).
The total value of an island is the sum of the values of all cells in the island.
Return the number of islands with a total value divisible by k.

 class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n, ans = len(grid), len(grid[0]), 0

        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    continue

                stack = [(i, j)]
                total = grid[i][j]
                grid[i][j] = 0

                while stack:
                    x, y = stack.pop()

                    for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0:
                            total += grid[nx][ny]
                            stack.append((nx, ny))
                            grid[nx][ny] = 0

                ans += total % k == 0

        return ans
