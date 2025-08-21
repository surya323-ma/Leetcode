Given an m x n binary matrix mat, return the number of submatrices that have all ones.
class Solution(object):
    def numSubmat(self, mat):
        m, n = len(mat), len(mat[0])
        # Preprocess: count consecutive ones in each row
        for i in range(m):
            for j in range(n):
                if mat[i][j] and j > 0:
                    mat[i][j] += mat[i][j - 1]

        total = 0
        # Count submatrices ending at (i, j)
        for i in range(m):
            for j in range(n):
                min_width = mat[i][j]
                for k in range(i, -1, -1):
                    if mat[k][j] == 0:
                        break
                    min_width = min(min_width, mat[k][j])
                    total += min_width
        return total
