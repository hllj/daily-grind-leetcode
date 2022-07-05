// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cur_cooldown = 0
        cur_hold = -float('inf')
        cur_not_hold = 0
        for x in prices:
            prev_cooldown, prev_hold, prev_not_hold = cur_cooldown, cur_hold, cur_not_hold
            cur_cooldown = max(prev_cooldown, prev_not_hold)
            cur_hold = max(prev_hold, prev_cooldown - x)
            cur_not_hold = max(prev_not_hold, prev_hold + x)
        return cur_not_hold