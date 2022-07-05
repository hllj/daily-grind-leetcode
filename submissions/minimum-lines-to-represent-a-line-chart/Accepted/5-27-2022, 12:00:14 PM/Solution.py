// https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart

import math
class Solution:
    def is_same_line(self, a, b):
        a0 = a[0]
        a1 = a[1]
        b0 = b[0]
        b1 = b[1]
        return (a0 * b1 == a1 * b0)
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        n = len(stockPrices)
        if n == 1:
            return 0
        stockPrices = sorted(stockPrices, key=lambda x: x[0])
        print(stockPrices)
        curr_line = 0
        curr_vec = None
        for i in range(1, n):
            x1 = stockPrices[i - 1][0]
            y1 = stockPrices[i - 1][1]
            x2 = stockPrices[i][0]
            y2 = stockPrices[i][1]
            u = x2 - x1
            v = y2 - y1
            new_vec = (x2 - x1, y2 - y1)
            print(new_vec)
            if curr_vec is None:
                curr_vec = new_vec
                curr_line = 1
            if self.is_same_line(curr_vec, new_vec) is False:
                curr_line += 1
                curr_vec = new_vec
        return curr_line