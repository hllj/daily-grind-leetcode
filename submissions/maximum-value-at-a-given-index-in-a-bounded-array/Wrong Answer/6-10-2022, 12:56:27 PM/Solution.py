// https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        l = 0
        r = maxSum
        res = -1
        while l <= r:
            m = (l + r) // 2
            sum_left = (m - 1) * m // 2
            if m - index - 1 >= 1:
                sum_left -= (m - index - 2) * (m - index - 1) // 2
            sum_right = (m - 1) * m // 2
            if m - (n - index) - 1 >= 1:
                sum_right -= (m - (n - index) - 1) * (m - (n - index)) // 2
            if sum_left + sum_right + m <= maxSum:
                res = m
                l = m + 1
            else:
                r = m - 1
        return res
        