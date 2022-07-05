// https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = sign * x
        r = 0
        while x > 0:
            d = x % 10
            r = r * 10 + d
            x = x // 10
        res = sign * r
        if (res < -2147483648 or res > 2147483647):
            return 0
        return res