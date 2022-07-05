// https://leetcode.com/problems/count-number-of-ways-to-place-houses

class Solution:
    def countHousePlacements(self, n: int) -> int:
        mod = int(1e9 + 7)
        if n == 1:
            return 4
        a = 0
        b = 1
        for i in range(n + 1):
            c = a + b
            a = b
            b = c
        return (c * c) % mod