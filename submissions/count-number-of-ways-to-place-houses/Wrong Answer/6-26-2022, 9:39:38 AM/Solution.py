// https://leetcode.com/problems/count-number-of-ways-to-place-houses

class Solution:
    def countHousePlacements(self, n: int) -> int:
        mod = int(1e9 + 7)
        return (n + 1) * (n + 1) % mod