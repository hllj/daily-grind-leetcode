// https://leetcode.com/problems/unique-paths-iii

class Solution:
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    cnt = 0
    def dfs(self, idx, u, v, avail, grid, t0, t1, n_empty, m, n):
        if u == t0 and v == t1:
            if (idx - 2 == n_empty):
                self.cnt += 1
        for k in range(4):
            u1, v1 = u + self.dx[k], v + self.dy[k]
            if (u1 < 0) or (u1 == m) or (v1 < 0) or (v1 == n) or grid[u1][v1] == -1:
                continue
            if avail[u1][v1] == True:
                avail[u1][v1] = False
                self.dfs(idx + 1, u1, v1, avail, grid, t0, t1, n_empty, m, n)
                avail[u1][v1] = True
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.cnt = 0
        m = len(grid)
        n = len(grid[0])
        s0, s1 = -1, -1
        t0, t1 = -1, -1
        n_empty = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    s0, s1 = i, j
                if grid[i][j] == 2:
                    t0, t1 = i, j
                if grid[i][j] == 0:
                    n_empty += 1

        avail = [[True for _ in range(n)] for _ in range(m)]
        avail[s0][s1] = False
        self.dfs(1, s0, s1, avail, grid, t0, t1, n_empty, m, n)
        return self.cnt