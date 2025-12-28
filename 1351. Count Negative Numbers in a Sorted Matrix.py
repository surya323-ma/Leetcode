iven a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row, col = m - 1, 0
        count = 0
    
        while row >= 0 and col < n:
            if grid[row][col] < 0:
                count += (n - col)   # all elements to the right are negative
                row -= 1             # move up
            else:
                col += 1             # move right
    
        return count
