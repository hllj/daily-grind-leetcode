// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        d = {}
        i = 0
        j = 0
        while i < n:
            x = s[i]
            if x in d:
                if d[x] > j:
                    j = d[x]
            d[x] = i
            res = max(res, i - j)
            i += 1
        return res
                