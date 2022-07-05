// https://leetcode.com/problems/minimum-falling-path-sum

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        f = [0] * m
        f1 = [0] * m
        for j in range(m):
            f[j] = matrix[0][j]
        for i in range(1, n):
            for j in range(m):
                f1[j] = matrix[i][j] + f[j]
                if j - 1 >= 0:
                    f1[j] = min(f1[j], matrix[i][j] + f[j - 1])
                if j + 1 < m:
                    f1[j] = min(f1[j], matrix[i][j] + f[j + 1])
            f = f1
        return min(f1)