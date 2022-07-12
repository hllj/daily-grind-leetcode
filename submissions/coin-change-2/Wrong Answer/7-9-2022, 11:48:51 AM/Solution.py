// https://leetcode.com/problems/coin-change-2

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        f = [[0 for _ in range(n + 1)] for _ in range(amount + 1)]
        for j in range(1, n + 1):
            f[0][j] = 1
        for s in range(1, amount + 1):
            for j in range(1, n + 1):
                f[s][j] = f[s][j - 1]
                for k in range(1, j + 1):
                    if s >= coins[k - 1]:
                        f[s][j] += f[s - coins[k - 1]][j]
        print(f)
        return f[amount][n - 1]