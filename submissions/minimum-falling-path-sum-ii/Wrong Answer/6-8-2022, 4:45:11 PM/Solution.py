// https://leetcode.com/problems/minimum-falling-path-sum-ii

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        f = [0] * m
        f1 = [0] * m
        inf = float('inf')
        for j in range(m):
            f[j] = grid[0][j]
        print(f)
        for i in range(1, n):
            for j in range(m):
                f1[j] = inf
                if j - 1 >= 0:
                    f1[j] = min(f1[j], grid[i][j] + f[j - 1])
                if j + 1 < m:
                    f1[j] = min(f1[j], grid[i][j] + f[j + 1])
            f,f1 = f1,f
        return min(f)