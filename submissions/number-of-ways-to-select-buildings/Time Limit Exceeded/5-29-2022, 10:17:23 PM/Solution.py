// https://leetcode.com/problems/number-of-ways-to-select-buildings

class Solution:
    def countsubseq(self, s, t, n, m):
        for i in range(1, n + 1):
            self.f[i][0] = 1
        for j in range(1, m + 1):
            self.f[0][j] = 0
        self.f[0][0] = 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    self.f[i][j] = self.f[i - 1][j - 1] + self.f[i - 1][j]
                else:
                    self.f[i][j] = self.f[i - 1][j]
        return self.f[n][m]
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        m = 3
        self.f = [[0] * (m + 1)] * (n + 1)
        a = self.countsubseq(s, '010', n, m)
        b = self.countsubseq(s, '101', n, m)
        return a + b
        
        
# s[i] == '0' -> office
# s[i] == '1' -> restaurant

# countsubseq '010' or '101'
# f(i, j): number of subseq from 1->i in s and 1->j in t
# f(0, j) = 0
# f(i, 0) = 1
# f(i, j) = f(i - 1, j) + f(i - 1, j - 1) if s[i] == s[j]
#         = f(i - 1, j) if s[i] != s[j]