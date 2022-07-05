// https://leetcode.com/problems/palindrome-partitioning-ii

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        f = [0 for _ in range(n + 1)]
        p = [[False for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            p[i][i] = True
        for i in range(1, n):
            p[i + 1][i] = True
        for i in range(2, n + 1):
            for j in range(i - 1, 0, -1):
                p[j][i] = (p[j + 1][i - 1]) and s[j - 1] == s[i - 1]
        inf = 2001
        for i in range(1, n + 1):
            f[i] = inf
            for j in range(i):
                if p[j + 1][i]:
                    f[i] = min(f[i], f[j] + 1)
        return f[n] - 1