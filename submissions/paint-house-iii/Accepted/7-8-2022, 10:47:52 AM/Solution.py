// https://leetcode.com/problems/paint-house-iii

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        inf = float('inf')
        f = [[[inf for _ in range(n + 1)] for _ in range(target + 1)] for _ in range(m + 1)]
        for c in range(1, n + 1):
            f[0][0][c] = 0
        for i in range(1, m + 1):
            for j in range(1, target + 1):
                for x in range(1, n + 1):
                    if houses[i - 1] != 0:
                        if houses[i - 1] == x:
                            for y in range(1, n + 1):
                                if y == x:
                                    f[i][j][x] = min(f[i][j][x], f[i - 1][j][y])
                                else:
                                    f[i][j][x] = min(f[i][j][x], f[i - 1][j - 1][y])
                        else:
                            f[i][j][x] = inf
                    else:
                        for y in range(1, n + 1):
                            if y == x:
                                f[i][j][x] = min(f[i][j][x], f[i - 1][j][x] + cost[i - 1][x - 1])
                            else:
                                f[i][j][x] = min(f[i][j][x], f[i - 1][j - 1][y] + cost[i - 1][x - 1])
        res = min(f[m][target][:])
        if res == inf:
            return -1
        return res
        