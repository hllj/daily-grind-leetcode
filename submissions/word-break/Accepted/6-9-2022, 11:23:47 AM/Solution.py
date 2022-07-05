// https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        f = [False] * (n + 1)
        f[0] = True
        for i in range(1, n + 1):
            f[i] = False
            for j in range(1, i + 1):
                sub = s[j - 1: i]
                if sub in wordDict:
                    f[i] = f[i] or f[j - 1]
        return f[n]