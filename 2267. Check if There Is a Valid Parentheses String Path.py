A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

It is ().
It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
It can be written as (A), where A is a valid parentheses string.
You are given an m x n matrix of parentheses grid. A valid parentheses string path in the grid is a path satisfying all of the following conditions:

The path starts from the upper left cell (0, 0).
The path ends at the bottom-right cell (m - 1, n - 1).
The path only ever moves down or right.
The resulting parentheses string formed by the path is valid.
Return true if there exists a valid parentheses string path in the grid. Otherwise, return false.

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        if (n + m - 1) % 2 or grid[0][0] != "(" or grid[-1][-1] != ")":
            return False

        from collections import deque
        q = deque([(0, 0, 1)])  # (i, j, balance of '(' )
        seen = {(0, 0, 1)}

        while q:
            i, j, bal = q.popleft()
            if bal < 0: continue
            if i == n - 1 and j == m - 1 and bal == 0:
                return True

            for ni, nj in ((i+1, j), (i, j+1)):
                if ni < n and nj < m:
                    nb = bal + (1 if grid[ni][nj] == "(" else -1)
                    state = (ni, nj, nb)
                    if nb >= 0 and state not in seen:
                        seen.add(state)
                        q.append(state)

        return False
