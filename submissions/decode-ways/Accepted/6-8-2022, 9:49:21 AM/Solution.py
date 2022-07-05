// https://leetcode.com/problems/decode-ways

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        f = [0] * (n + 1)
        if s[0] == '0':
            return 0
        f[0] = 1
        for i in range(1, n + 1):
            f[i] = 0
            if (s[i - 1] >= '1' and s[i - 1] <= '9'):
                f[i] += f[i - 1]
            if (i >= 2):
                v = s[i - 2] + s[i - 1]
                if (v >= '1' and v <= '26'):
                    f[i] += f[i - 2]
        return f[n]