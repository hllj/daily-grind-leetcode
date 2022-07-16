// https://leetcode.com/problems/max-area-of-island

class Solution:
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    def dfs(self, grid, x, y, island):
        self.avail[x][y] = False
        island.append((x, y))
        for i in range(4):
            new_x = x + self.dx[i]
            new_y = y + self.dy[i]
            if (new_x < 0) or (new_x == self.n) or (new_y < 0) or (new_y == self.m):
                continue
            if (self.avail[new_x][new_y] is True) and (grid[new_x][new_y] == 1):
                self.dfs(grid, new_x, new_y, island)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.n = len(grid)
        self.m = len(grid[0])
        self.avail = [[True for _ in range(self.m)] for _ in range(self.n)]
        res = 0
        for i in range(self.n):
            for j in range(self.m):
                if (self.avail[i][j] is True) and (grid[i][j] == 1):
                    island = []
                    self.dfs(grid, i, j, island)
                    res = max(res, len(island))
        return res