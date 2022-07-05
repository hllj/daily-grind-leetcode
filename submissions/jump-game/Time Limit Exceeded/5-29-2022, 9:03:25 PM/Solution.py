// https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = [False] * n
        memo[0] = True
        for i in range(1, n):
            memo[i] = False
            for j in range(0, i):
                if memo[j] is True and (j + nums[j] >= i):
                    memo[i] = True
                    break
        return memo[n - 1]
        
        