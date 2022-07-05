// https://leetcode.com/problems/perfect-squares

class Solution:
    def numSquares(self, n: int) -> int:
        f = {}
        f[0] = 0
        inf = float('inf')
        for i in range(1, n + 1):
            res = inf
            x = 1
            while x * x <= i:
                res = min(res, f[i - x * x] + 1)
                x += 1
            f[i] = res
        return f[n]