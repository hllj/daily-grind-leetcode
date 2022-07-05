// https://leetcode.com/problems/jump-game

class Solution:
    memo = {}
    def jump(self, u, nums, n):
        if self.memo[u] is True:
            return
        self.memo[u] = True
        for i in range(1, nums[u] + 1):
            if (u + i < n):
                self.jump(u + i, nums, n)
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        for u in range(n):
            self.memo[u] = False
        self.jump(0, nums, n)
        return self.memo[n - 1]
        
        