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
        return sign * r