// https://leetcode.com/problems/shortest-path-in-binary-matrix

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0:
            return -1
        f = [[-1 for _ in range(n)] for _ in range(n)]
        q = [(0, 0)]
        visited = set()
        visited.add((0, 0))
        f[0][0] = 1
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        while len(q) > 0:
            (u, v) = q.pop(0)
            for k in range(8):
                u1, v1 = u + dx[k], v + dy[k]
                if u1 < 0 or u1 == n or v1 < 0 or v1 == n:
                    continue
                if (u1, v1) not in visited and grid[u1][v1] == 0:
                    q.append((u1, v1))
                    visited.add((u1, v1))
                    f[u1][v1] = f[u][v] + 1
        return f[n - 1][n - 1]