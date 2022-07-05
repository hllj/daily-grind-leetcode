// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = -float('inf')
        not_hold = 0
        for x in prices:
            prev_hold, prev_not_hold = hold, not_hold
            hold = max(prev_hold, prev_not_hold - x)
            not_hold = max(prev_not_hold, prev_hold + x - fee)
        return not_hold