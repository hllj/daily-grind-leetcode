// https://leetcode.com/problems/remove-palindromic-subsequences

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        n = len(s)
        for i in range(n // 2):
            if s[i] != s[n - i - 1]:
                return 2
        return 1