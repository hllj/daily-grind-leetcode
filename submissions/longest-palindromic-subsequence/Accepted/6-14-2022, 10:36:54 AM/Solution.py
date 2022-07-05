// https://leetcode.com/problems/longest-palindromic-subsequence

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        f = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(n):
            f[i][i] = 1
            for j in range(i - 1, -1, -1):
                if s[i] == s[j]:
                    f[j][i] = f[j + 1][i - 1] + 2
                else:
                    f[j][i] = max(f[j + 1][i], f[j][i - 1])
        return f[0][n - 1]