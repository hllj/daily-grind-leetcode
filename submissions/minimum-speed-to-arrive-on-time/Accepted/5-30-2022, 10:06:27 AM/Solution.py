// https://leetcode.com/problems/minimum-speed-to-arrive-on-time

import math
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        l = 1
        r = int(1e7)
        res = -1
        while l <= r:
            m = (l + r) // 2
            s = 0
            for i in range(n - 1):
                s += math.ceil(dist[i] / m)
            s += dist[-1] / m
            if s <= hour:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res