// https://leetcode.com/problems/interleaving-string

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s1 == "":
            return s2 == s3
        if s2 == "":
            return s1 == s3
        n = len(s1)
        m = len(s2)
        c = len(s3)
        f = [[[False for _ in range(m + 1)] for _ in range(n + 1)] for _ in range(c + 1)]
        for j in range(1, n + 1):
            if s3[:j] == s1[:j]:
                f[j][j][0] = True
        for k in range(1, m + 1):
            if s3[:k] == s2[:k]:
                f[k][0][k] = True
        f[0][0][0] = True
        for i in range(1, c + 1):
            for j in range(1, n + 1):
                for k in range(1, m + 1):
                    if s3[i - 1] == s1[j - 1]:
                        f[i][j][k] |= f[i - 1][j - 1][k]
                    elif s3[i - 1] == s2[k - 1]:
                        f[i][j][k] |= f[i - 1][j][k - 1]
                    else:
                        f[i][j][k] = False
        return f[c][n][m]