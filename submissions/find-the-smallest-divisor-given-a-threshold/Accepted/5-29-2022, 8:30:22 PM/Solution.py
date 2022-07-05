// https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold

import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = max(nums)
        res = -1
        while l <= r:
            m = (l + r) // 2
            s = 0
            for x in nums:
                s += int(math.ceil(x / m))
            if s <= threshold:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
        