// https://leetcode.com/problems/interleaving-string

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s1 == "":
            return s2 == s3
        if s2 == "":
            return s1 == s3
        n = len(s1)
        m = len(s2)
        f = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        for j in range(1, n + 1):
            if s3[:j] == s1[:j]:
                f[j][0] = True
        for k in range(1, m + 1):
            if s3[:k] == s2[:k]:
                f[0][k] = True
        f[0][0] = True
        for j in range(1, n + 1):
            for k in range(1, m + 1):
                i = j + k
                if s3[i - 1] == s1[j - 1]:
                    f[j][k] |= f[j - 1][k]
                if s3[i - 1] == s2[k - 1]:
                    f[j][k] |= f[j][k - 1]
        return f[n][m]