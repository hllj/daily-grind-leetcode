// https://leetcode.com/problems/minimum-path-cost-in-a-grid

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        f = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(n):
            f[0][j] = grid[0][j]
        inf = float('inf')
        for i in range(1, m):
            for j in range(n):
                f[i][j] = inf
                for k in range(n):
                    cost = moveCost[grid[i - 1][k]][j] + grid[i][j]
                    f[i][j] = min(f[i][j], f[i - 1][k] + cost)
        return min(f[m - 1][:])