// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        f = [0] * n
        for i in range(1, n):
            for j in range(0, i):
                profit = prices[i] - prices[j]
                if j >= 2:
                    profit += f[j - 2]
                print(j, profit)
                f[i] = max(f[i], profit)
            print(i, f[i], profit)
        return f[n - 1]