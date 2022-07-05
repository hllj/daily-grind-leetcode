// https://leetcode.com/problems/minimum-speed-to-arrive-on-time

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        l = 1
        r = max(dist)
        res = -1
        while l <= r:
            m = (l + r) // 2
            s = 0
            for x in dist:
                s += x / m
            if s <= hour:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res