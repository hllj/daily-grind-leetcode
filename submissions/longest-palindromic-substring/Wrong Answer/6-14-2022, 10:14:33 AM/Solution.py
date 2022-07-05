// https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        f = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(n):
            f[i][i] = 1
            for j in range(i - 1, -1, -1):
                if s[i] == s[j]:
                    f[j][i] = f[j + 1][i - 1] + 2
                else:
                    f[j][i] = max(f[j + 1][i], f[j][i - 1])
        max_len = f[0][n - 1]
        for i in range(n):
            for j in range(i, -1, -1):
                if i - j + 1 == max_len and f[j][i] == max_len:
                    return s[j:i+1]