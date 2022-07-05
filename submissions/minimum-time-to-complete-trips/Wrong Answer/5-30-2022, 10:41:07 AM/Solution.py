// https://leetcode.com/problems/minimum-time-to-complete-trips

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        n = len(time)
        l = 1
        r = int(1e13)
        res = 0
        while l <= r:
            m = (l + r) // 2
            total = 0
            for x in time:
                total += m // x
            if total >= totalTrips:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res