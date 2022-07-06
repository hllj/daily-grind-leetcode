// https://leetcode.com/problems/wildcard-matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        f = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        f[0][0] = True
        for j in range(1, m + 1):
            if p[j - 1] == '*':
                f[0][j] = f[0][j - 1]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if (s[i - 1] == p[j - 1] or p[j - 1] == '?'):
                    f[i][j] = f[i - 1][j - 1]
                elif p[j - 1] == '*':
                    f[i][j] = f[i - 1][j] or f[i][j - 1]
                else:
                    f[i][j] = False
        return f[n][m]