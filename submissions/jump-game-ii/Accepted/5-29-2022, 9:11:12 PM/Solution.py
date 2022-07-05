// https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        inf = int(1e4) + 1
        f = [inf] * n
        f[0] = 0
        prev = 0
        for i in range(0, n):
            for j in range(prev, i):
                if (nums[j] + j >= i):
                    f[i] = min(f[i], f[j] + 1)
                    prev = j
                    break
        return f[n - 1]