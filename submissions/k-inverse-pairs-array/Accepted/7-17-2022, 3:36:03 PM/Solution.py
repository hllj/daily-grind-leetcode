// https://leetcode.com/problems/k-inverse-pairs-array

class Solution:
    modulo = int(1e9 + 7)
    def kInversePairs(self, n: int, k: int) -> int:
        f = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(k + 1):
                if j == 0:
                    f[i][j] = 1
                else:
                    val = f[i - 1][j]
                    if j - i >= 0:
                        val = (val - f[i - 1][j - i] + self.modulo) % self.modulo
                    f[i][j] = (f[i][j - 1] + val) % self.modulo
        res = f[n][k]
        if k > 0:
            res = (res - f[n][k - 1] + self.modulo) % self.modulo
        return res