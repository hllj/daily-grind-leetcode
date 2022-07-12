// https://leetcode.com/problems/jump-game-vi

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = [0 for _ in range(n)]
        f[0] = nums[0]
        for i in range(1, n):
            f[i] = -float('inf')
            for t in range(1, k + 1):
                if i - t >= 0:
                    # print(i - t, f[i - t], nums[i - t])
                    f[i] = max(f[i], f[i - t] + nums[i])
            # print(i, f[i])
        # print(f)
        return f[n - 1]