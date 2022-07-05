// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        min_prices = [0] * (n)
        min_prices[0] = prices[0]
        for i in range(1, n):
            min_prices[i] = min(min_prices[i - 1], prices[i])
        max_profit = 0
        for i in range(1, n):
            max_profit = max(max_profit, prices[i] - min_prices[i - 1])
        return max_profit