// https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique

class Solution:
    def minDeletions(self, s: str) -> int:
        d = {}
        for c in range(26):
            d[c] = 0
        for x in s:
            d[ord(x) - ord('a')] += 1
        b = []
        for c in range(26):
            if d[c] != 0:
                b.append(d[c])
        b = sorted(b, reverse=True)
        n = len(b)
        idx = -1
        s = set()
        res = 0
        for i in range(n):
            while b[i] in s and b[i] > 0:
                b[i] -= 1
                res += 1
            s.add(b[i])
        return res
            
            
        