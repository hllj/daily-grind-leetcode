// https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        for i in range(1, n):
            chalk[i] = chalk[i - 1] + chalk[i]
        k %= chalk[n - 1]
        l = 0
        r = n - 1
        res = -1
        while l <= r:
            m = (l + r) // 2
            if chalk[m] > k:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res