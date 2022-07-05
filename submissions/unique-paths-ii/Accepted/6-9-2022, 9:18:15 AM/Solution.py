// https://leetcode.com/problems/unique-paths-ii

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        f = [[0 for _ in range(n)] for _ in range(m)]
        v = 1
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                v = 0
            f[i][0] = v
        v = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                v = 0
            f[0][j] = v
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    f[i][j] = 0
                else:
                    f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]