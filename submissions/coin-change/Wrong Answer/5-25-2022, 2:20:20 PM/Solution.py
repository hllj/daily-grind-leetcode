// https://leetcode.com/problems/coin-change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        f = [0] * (amount + 1)
        for s in range(1, amount + 1):
            f[s] = int(1e10)
            for x in coins:
                f[s] = min(f[s], f[s - x] + 1)
        if f[amount] == int(1e10):
            return 0
        else:
            return f[amount]
        