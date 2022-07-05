// https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        f = [[False for _ in range(n + 1)] for _ in range(n + 1)]
        for j in range(n):
            for i in range(n):
                if j >= i:
                    f[j][i] = True
                else:
                    f[j][i] = False
        max_len = 0
        max_i = -1
        max_j = -1
        for i in range(n):
            for j in range(i, -1, -1):
                if s[i] == s[j]:
                    f[j][i] = f[j][i] or f[j + 1][i - 1]
                else:
                    f[j][i] = False
                if f[j][i] == True and i - j + 1 > max_len:
                    max_len = i - j + 1
                    max_i = i
                    max_j = j
        return s[max_j: max_i + 1]