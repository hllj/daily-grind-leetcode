// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 1
        for i in range(n):
            t = set()
            for j in range(i, n):
                t.add(s[j])
                # print(i, j, len(t))
                if len(t) == j - i + 1:
                    res = max(res, j - i + 1)
        return res
                