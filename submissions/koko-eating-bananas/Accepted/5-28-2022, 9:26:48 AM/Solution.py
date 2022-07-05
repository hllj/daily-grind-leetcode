// https://leetcode.com/problems/koko-eating-bananas

import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = -1
        while l <= r:
            m = (l + r) // 2
            cnt_h = 0
            for x in piles:
                cnt_h += int(math.ceil(x / m))
            if cnt_h <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res