// https://leetcode.com/problems/unique-binary-search-trees

class Solution:
    @cache
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 1
        res = 0
        for i in range(1, n + 1):
            res += self.numTrees(i - 1) * self.numTrees(n - i)
        return res
            