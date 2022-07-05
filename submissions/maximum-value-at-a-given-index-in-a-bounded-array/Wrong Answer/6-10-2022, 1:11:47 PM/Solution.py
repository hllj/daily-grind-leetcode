// https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array

class Solution:
    def calculate(self, m, index, n, maxSum):
        if index >= 1:
            sum_left = (m - 1) * m // 2
            if (m - index - 1 >= 1):
                sum_left -= (m - index - 1) * (m - index) // 2
        else:
            sum_left = 0
        print(sum_left)
        if n - index - 1 >= 1:
            sum_right = (m - 1) * m // 2
            if (m - (n - index) >= 1):
                sum_right -= (m - (n - index)) * (m - (n - index) + 1) // 2
        else:
            sum_right = 0
        print(sum_right)
        return sum_left + sum_right + m <= maxSum
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        l = 0
        r = maxSum
        res = -1
        print(self.calculate(3, index, n, maxSum))
        # print(self.calculate(3, index, n, maxSum))
        while l <= r:
            m = (l + r) // 2
            sum_left = (m - 1) * m // 2
            if m - index - 1 >= 1:
                sum_left -= (m - index - 2) * (m - index - 1) // 2
            sum_right = (m - 1) * m // 2
            if m - (n - index) - 1 >= 1:
                sum_right -= (m - (n - index) - 1) * (m - (n - index)) // 2
            if self.calculate(m, index, n, maxSum):
                res = m
                l = m + 1
            else:
                r = m - 1
        return res
        