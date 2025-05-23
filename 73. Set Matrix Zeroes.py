Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
#code here

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        li = set()
        lj = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    li.add(i)
                    lj.add(j)
        
        for m in range(len(matrix)):
            if m in li:
                for k in range(len(matrix[i])):
                    matrix[m][k] = 0
            else:
                for n in range(len(matrix[i])):
                    if n in lj:
                        matrix[m][n] = 0
