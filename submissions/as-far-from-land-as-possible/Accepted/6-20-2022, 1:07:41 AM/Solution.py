// https://leetcode.com/problems/as-far-from-land-as-possible

class Solution:
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        avail = [[True for _ in range(n)] for _ in range(n)]
        f = [[0 for _ in range(n)] for _ in range(n)]
        q = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    f[i][j] = 0
                    q.append((i, j))
                    avail[i][j] = False
        while len(q) > 0:
            q1 = []
            while len(q) > 0:
                (u, v) = q.pop(0)
                for k in range(4):
                    u1, v1 = u + self.dx[k], v + self.dy[k]
                    if u1 < 0 or u1 == n or v1 < 0 or v1 == n:
                        continue
                    if avail[u1][v1] is True and grid[u1][v1] == 0:
                        q1.append((u1, v1))
                        avail[u1][v1] = False
                        f[u1][v1] = f[u][v] + 1
            q, q1 = q1, q
        res = 0
        for i in range(n):
            for j in range(n):
                res = max(res, f[i][j])
        if res == 0:
            return -1
        else:
            return res