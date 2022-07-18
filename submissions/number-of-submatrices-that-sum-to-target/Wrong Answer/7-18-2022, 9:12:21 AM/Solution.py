// https://leetcode.com/problems/number-of-submatrices-that-sum-to-target

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n = len(matrix)
        for i in range(1, n):
            matrix[i][0] += matrix[i - 1][0]
        for j in range(1, n):
            matrix[0][j] += matrix[0][j - 1]
        for i in range(1, n):
            for j in range(1, n):
                matrix[i][j] = matrix[i][j] + matrix[i - 1][j] + matrix[i][j - 1] - matrix[i - 1][j - 1]
                
        def sumRegion(row1, col1, row2, col2):
            s = matrix[row2][col2]
            if col1 - 1 >= 0:
                s -= matrix[row2][col1 - 1]
            if row1 - 1 >= 0:
                s -= matrix[row1 - 1][col2]
            if row1 - 1 >= 0 and col1 - 1 >= 0:
                s += matrix[row1 - 1][col1 - 1]
            return s
        res = 0
        for i1 in range(0, n):
            for j1 in range(0, n):
                for i2 in range(i1, n):
                    for j2 in range(j1, n):
                        if sumRegion(i1, j1, i2, j2) == target:
                            res += 1
        return res
        