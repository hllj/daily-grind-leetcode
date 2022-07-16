// https://leetcode.com/problems/out-of-boundary-paths

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        f = [[[0 for _ in range(maxMove + 1)] for _ in range(n)] for _ in range(m)]
        f[startRow][startColumn][0] = 1
        res = 0
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        modulo = int(1e9 + 7)
        for k in range(0, maxMove):
            for i in range(m):
                for j in range(n):
                    count = 0
                    for x in range(4):
                        prev_i = i + dx[x]
                        prev_j = j + dy[x]
                        if not (prev_i < 0 or prev_i == m or prev_j < 0 or prev_j == n):
                            if k - 1 >= 0:
                                f[i][j][k] += f[prev_i][prev_j][k - 1]
                        else:
                            count += 1
                    res += f[i][j][k] * count
        return res % modulo