// https://leetcode.com/problems/fibonacci-number

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        a = 1
        b = 1
        for i in range(3, n + 1):
            c = a + b
            a = b
            b = c
        return b