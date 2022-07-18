// https://leetcode.com/problems/k-inverse-pairs-array

class Solution:
    modulo = int(1e9 + 7)
    @cache
    def kInversePairs(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if k == 0:
            return 1
        inv = 0
        for i in range(min(k, n - 1) + 1):
            inv = (inv + self.kInversePairs(n - 1, k - i)) % self.modulo
        return inv 