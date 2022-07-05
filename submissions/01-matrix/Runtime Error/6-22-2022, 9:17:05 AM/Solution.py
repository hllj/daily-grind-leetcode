// https://leetcode.com/problems/01-matrix

class Solution:
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        avail = [[True for _ in range(m)] for _ in range(n)]
        f = [[0 for _ in range(m)] for _ in range(n)]
        q = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    f[i][j] = 0
                    q.append((i, j))
                    avail[i][j] = False
        # print(q)
        while len(q) > 0:
            q1 = []
            while len(q) > 0:
                (u, v) = q.pop(0)
                for k in range(4):
                    u1, v1 = u + self.dx[k], v + self.dy[k]
                    if u1 < 0 or u1 == m or v1 < 0 or v1 == n:
                        continue
                    if avail[u1][v1] is True and mat[u1][v1] == 1:
                        f[u1][v1] = f[u][v] + 1
                        q1.append((u1, v1))
                        avail[u1][v1] = False
            q1, q = q, q1
        return f