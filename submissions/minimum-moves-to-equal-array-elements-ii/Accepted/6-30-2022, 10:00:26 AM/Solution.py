// https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii

import math
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if n == 2:
            return abs(nums[1] - nums[0])
        nums = sorted(nums)
        f = [0 for _ in range(n + 1)]
        f[0] = 0
        for i in range(1, n + 1):
            f[i] = f[i - 1] + nums[i - 1]
        print(f)
        res = float('inf')
        for n1 in range(1, n):
            s1 = f[n1]
            s2 = f[n] - f[n1]
            if 2 * n1 != n:
                x = min(max(math.floor((s1 - s2) / (2 * n1 - n)), nums[n1 - 1]), nums[n1])
                cnt = abs(n1 * x - s1) + abs(s2 - (n - n1) * x)
                # print(n1, x, cnt)
                res = min(res, cnt)
        return res