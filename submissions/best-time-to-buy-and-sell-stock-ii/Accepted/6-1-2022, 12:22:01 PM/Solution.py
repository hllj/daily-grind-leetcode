// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        idx = 0
        max_profit = 0
        while idx < n:
            while (idx + 1 < n and prices[idx + 1] <= prices[idx]):
                idx += 1
            buy = prices[idx]
            while (idx + 1 < n and prices[idx + 1] >= prices[idx]):
                idx += 1
            sell = prices[idx]
            max_profit += sell - buy
            idx += 1
        return max_profit
            