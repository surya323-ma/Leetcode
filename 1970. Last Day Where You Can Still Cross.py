There is a 1-based binary matrix where 0 represents land and 1 represents water. You are given integers row and col representing the number of rows and columns in the matrix, respectively.
Initially on day 0, the entire matrix is land. However, each day a new cell becomes flooded with water. You are given a 1-based 2D array cells, where cells[i] = [ri, ci] represents that on the ith day, the cell on the rith row and cith column (1-based coordinates) will be covered with water (i.e., changed to 1).
You want to find the last day that it is possible to walk from the top to the bottom by only walking on land cells. You can start from any cell in the top row and end at any cell in the bottom row. You can only travel in the four cardinal directions (left, right, up, and down).

Return the last day where it is possible to walk from the top to the bottom by only walking on land cells.

from typing import List
from collections import deque

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def canCross(day: int) -> bool:
            water = set(map(tuple, cells[:day]))
            q = deque([(0, c) for c in range(col) if (1, c+1) not in water])
            seen = set(q)
            while q:
                r, c = q.popleft()
                if r == row-1: return True
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < row and 0 <= nc < col and (nr+1,nc+1) not in water and (nr,nc) not in seen:
                        seen.add((nr,nc))
                        q.append((nr,nc))
            return False

        l, r, ans = 1, len(cells), 0
        while l <= r:
            m = (l+r)//2
            if canCross(m):
                ans = m; l = m+1
            else:
                r = m-1
        return ans
