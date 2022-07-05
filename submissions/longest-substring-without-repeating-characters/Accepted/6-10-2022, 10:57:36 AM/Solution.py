// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = -1
        d = {}
        i = 0
        j = -1
        while i < n:
            x = s[i]
            if x in d:
                if d[x] > j:
                    j = d[x]
            d[x] = i
            if j == -1:
                res = max(res, i + 1)
            else:
                res = max(res, i - j)
            i += 1
        if res == -1:
            return 0
        return res
                