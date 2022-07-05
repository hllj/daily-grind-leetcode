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
            if x not in d:
                d[x] = [i]
            else:
                d[x].append(i)
            if len(d[x]) >= 2:
                for p in d[x]:
                    if (p > j):
                        j = p
            res = max(res, i - j + 1)
            i += 1
        return res
                