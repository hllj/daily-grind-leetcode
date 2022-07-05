// https://leetcode.com/problems/minimum-falling-path-sum

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        f = [0] * m
        f1 = [0] * m
        for j in range(m):
            f[j] = matrix[0][j]
        print(f)
        for i in range(1, n):
            for j in range(m):
                f1[j] = matrix[i][j] + min(f[j], f[max(0, j - 1)], f[min(m - 1, j + 1)])
            f,f1 = f1,f
            print(f)
        return min(f)