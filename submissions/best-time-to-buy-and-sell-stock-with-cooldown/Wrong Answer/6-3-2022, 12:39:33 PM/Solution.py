// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        f = [0] * n
        res = 0
        for i in range(1, n):
            for j in range(0, i):
                profit = prices[i] - prices[j]
                if j >= 2:
                    profit += f[j - 2]
                print('profit', i, j, profit)
                f[i] = max(f[i], profit)
            res = max(res, f[i])
        return res