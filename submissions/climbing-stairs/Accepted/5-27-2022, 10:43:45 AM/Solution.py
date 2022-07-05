// https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        a = 1
        b = 1
        c = None
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b