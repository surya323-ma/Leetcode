You are given an n x n square matrix of integers grid. Return the matrix such that:

The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order.
The diagonals in the top-right triangle are sorted in non-decreasing order.
  class Solution(object):
    def sortMatrix(self, grid):
        n = len(grid)

        def get_diag(r, c):
            return [grid[i][j] for i, j in zip(range(r, n), range(c, n))]

        def set_diag(r, c, vals):
            for i, j, v in zip(range(r, n), range(c, n), vals):
                grid[i][j] = v

        for r in range(n):
            vals = sorted(get_diag(r, 0), reverse=True)
            set_diag(r, 0, vals)

        for c in range(1, n):
            vals = sorted(get_diag(0, c))
            set_diag(0, c, vals)

        return grid
