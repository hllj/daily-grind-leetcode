// https://leetcode.com/problems/coin-change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        f = [1e9] * (amount + 1)
        f[0] = 0
        for s in range(1, amount + 1):
            for x in coins:
                if s >= x:
                    f[s] = min(f[s], f[s - x] + 1)
        if f[amount] == int(1e10):
            return -1
        else:
            return f[amount]
        