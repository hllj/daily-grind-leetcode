// https://leetcode.com/problems/number-of-enclaves

class Solution:
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    def dfs(self, x, y, n, m, grid, island, avail):
        island.append((x, y))
        avail[x][y] = False
        for k in range(4):
            x1 = x + self.dx[k]
            y1 = y + self.dy[k]
            if (x1 < 0) or (x1 == n) or (y1 < 0) or (y1 == m):
                self.is_reach_bound = True
                continue
            if avail[x1][y1] is True and grid[x1][y1] == 1:
                self.dfs(x1, y1, n, m, grid, island, avail)
        
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        avail = [[True for _ in range(m)] for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and avail[i][j] is True:
                    island = []
                    self.is_reach_bound = False
                    self.dfs(i, j, n, m, grid, island, avail)
                    # print('res', island, self.is_reach_bound)
                    if self.is_reach_bound is False:
                        res += len(island)
        return res