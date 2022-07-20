// https://leetcode.com/problems/number-of-matching-subsequences

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while (i < len(s) and j < len(t)):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(s)
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res = []
        for word in words:
            if self.isSubsequence(word, s):
                res.append(word)
        return len(res)