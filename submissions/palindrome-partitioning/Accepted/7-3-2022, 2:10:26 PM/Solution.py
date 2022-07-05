// https://leetcode.com/problems/palindrome-partitioning

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        f = [None for _ in range(n + 1)]
        f[0] = [['']]
        p = [[False for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            p[i][i] = True
        for i in range(1, n):
            p[i + 1][i] = True
        for i in range(2, n + 1):
            for j in range(i - 1, 0, -1):
                p[j][i] = (p[j + 1][i - 1]) and s[j - 1] == s[i - 1]
        for i in range(1, n + 1):
            f[i] = []
            for j in range(i):
                if p[j + 1][i]:
                    for x in f[j]:
                        f[i].append(x + [s[j: i]])
        res = []
        for part in f[n]:
            part.remove('')
            res.append(part)
        return res