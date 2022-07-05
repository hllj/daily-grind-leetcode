// https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii

import math
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        res = float('inf')
        for x in range(min(nums), max(nums)):
            cnt = 0
            for i in nums:
                cnt += abs(i - x)
                if cnt >= res:
                    break
            res = min(res, cnt)
            # print(x, cnt)
        return res