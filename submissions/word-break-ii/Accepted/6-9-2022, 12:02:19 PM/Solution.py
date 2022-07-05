// https://leetcode.com/problems/word-break-ii

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        f = [False] * (n + 1)
        f[0] = True
        ch = [[] for _ in range(n + 1)]
        ch[0] = ['']
        for i in range(1, n + 1):
            f[i] = False
            ch[i] = []
            for j in range(1, i + 1):
                sub = s[j - 1: i]
                if sub in wordDict:
                    f[i] = f[i] or f[j - 1]
                    for x in ch[j - 1]:
                        ch[i].append(x + ' ' + sub)
        res = []
        for x in ch[n]:
            res.append(x.strip())
        return res