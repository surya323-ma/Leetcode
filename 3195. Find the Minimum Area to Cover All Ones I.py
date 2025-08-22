You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area, such that all the 1's in grid lie inside this rectangle.

Return the minimum possible area of the rectangle.
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        top, bottom = rows, -1
        left, right = cols, -1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    top = min(top, r)
                    bottom = max(bottom, r)
                    left = min(left, c)
                    right = max(right, c)

    # If no 1s were found, return 0
        if bottom == -1:
            return 0

        return (bottom - top + 1) * (right - left + 1)
