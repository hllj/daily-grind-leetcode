// https://leetcode.com/problems/as-far-from-land-as-possible

class Solution:
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        f = [[0 for _ in range(n)] for _ in range(n)]
        avail = [[True for _ in range(n)] for _ in range(n)]
        q = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    for k in range(4):
                        u, v = i + self.dx[k], j + self.dy[k]
                        if u < 0 or u == n or v < 0 or v == n:
                            continue
                        q.append((u, v))
                        f[u][v] = 1
        step = 1
        while len(q) > 0:
            step += 1
            q1 = []
            while len(q) > 0:
                (u, v) = q.pop(0)
                avail[u][v] = False
                for k in range(4):
                    u1, v1 = u + self.dx[k], v + self.dy[k]
                    if u1 < 0 or u1 == n or v1 < 0 or v1 == n:
                        continue
                    if avail[u1][v1] is True and grid[u1][v1] == 0:
                        f[u1][v1] = step
                        q1.append((u1, v1))
            q = q1
        print(f)
        res = 1
        for i in range(n):
            for j in range(n):
                res = max(res, f[i][j])
        if res == 1:
            return -1
        else:
            return res