// https://leetcode.com/problems/number-of-distinct-roll-sequences

import math

class Solution:
    def distinctSequences(self, n: int) -> int:
        if n == 1:
            return 6
        modulo = int(1e9 + 7)
        f = [[[0 for _ in range(6)] for _ in range(6)] for _ in range(n + 1)]
        for j in range(6):
            for k in range(6):
                f[2][j][k] = 0
                if math.gcd(j + 1, k + 1) == 1 and j != k:
                    f[2][j][k] = 1
        for i in range(3, n + 1):
            for j in range(6):
                for k in range(6):
                    f[i][j][k] = 0
                    # print('---')
                    # print(i, j + 1, k + 1)
                    for j0 in range(6):
                        if j != k and math.gcd(j + 1, k + 1) == 1 and j0 != k and math.gcd(j0 + 1, j + 1) == 1:
                            f[i][j][k] += f[i - 1][j0][j]
                            # print('check', j0 + 1)
        res = 0
        for j in range(6):
            for k in range(6):
                print(j + 1, k + 1, f[n][j][k])
                res += f[n][j][k]
        return res % modulo
        