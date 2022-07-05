// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = [0] * (n + 1)
        for i in range(1, n + 1):
            max_profit[i] = max_profit[i - 1]
            for j in range(1, i):
                max_profit[i] = max(max_profit[i], max_profit[j] + max(prices[j:i]) - min(prices[j:i]))
        return max_profit[n]